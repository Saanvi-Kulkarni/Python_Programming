import psutil
import sys
import os
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
load_dotenv()   

def ThreadMonitor(fobj):
    Border = "-"*50
    fobj.write("\nThread Monitoring Report\n")
    fobj.write(Border + "\n")
    for proc in psutil.process_iter():
        try:
            ProcessName = proc.name()
            PID         = proc.pid
            ThreadCount = proc.num_threads()      
            fobj.write("Process Name : %s\n" % ProcessName)
            fobj.write("PID          : %s\n" % PID)
            fobj.write("Threads      : %s\n" % ThreadCount)
            fobj.write(Border + "\n")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def CreateLog(FolderName, ReceiverMail):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os. path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")        # directory does not exit
            return
 
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name  : ",FileName)

    fobj = open(FileName, "w")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log create at : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------ System Report -------------------\n")

    # print("CPU usage : ", psutil.cpu_percent())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    # print("RAM usage : ", mem.percent)
    fobj.write("RAM usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process log
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Username : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write("RSS : %.2f MB\n" % info.get("rss"))
        fobj.write("VMS : %.2f MB\n" % info.get("vms"))
        fobj.write("Open Files : %s\n" % info.get("open_files"))
        fobj.write(Border+"\n")

    # Thread Monitor log
    ThreadMonitor(fobj)            
    TopMemoryProcesses(fobj) 

    fobj.write(Border+"\n")
    fobj.write("---------------- End of Log file -----------------\n")
    fobj.write(Border+"\n")
    fobj.close()                              
    SendEmail(ReceiverMail, FileName, Data)

def ProcessScan():
    listprocess = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time"])
                    
            #convert create_time
            try: 
                info["create_time"] = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            try:
                info["threads"] = proc.num_threads()
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                info["threads"] = 0
            try:
                info["open_files"] = len(proc.open_files())
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                info["open_files"] = "Access Denied"
            try:
                mem_info = proc.memory_info()
                info["rss"] = mem_info.rss / (1024 * 1024)
                info["vms"] = mem_info.vms / (1024 * 1024)
            except (psutil.AccessDenied, psutil.NoSuchProcess):
                info["rss"] = 0
                info["vms"] = 0
            
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def TopMemoryProcesses(fobj):
    Border = "-"*50
    fobj.write("\nTop 10 Memory Consuming Processes\n")
    fobj.write(Border + "\n")
    ProcessList = []
    for proc in psutil.process_iter():
        try:
            mem_info = proc.memory_info()
            ProcessList.append((proc.name(), proc.pid, mem_info.rss / (1024*1024)))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    ProcessList.sort(key=lambda x: x[2], reverse=True)
    for Name, PID, RSS in ProcessList[:10]:
        fobj.write("Name : %s | PID : %s | RSS : %.2f MB\n" % (Name, PID, RSS))
    fobj.write(Border + "\n")

def SendEmail(ReceiverMail, LogFile, Data):
    try:
        SenderMail     = os.getenv("SENDER_MAIL")
        SenderPassword = os.getenv("SENDER_PASSWORD")

        if not SenderMail or not SenderPassword:
            print("Error : .env file missing or SENDER_MAIL/SENDER_PASSWORD not set")
            return

        TotalProcesses = len(Data)
        TopCPU         = sorted(Data, key=lambda x: x.get("cpu_percent", 0),    reverse=True)[:3]
        TopMemory      = sorted(Data, key=lambda x: x.get("memory_percent", 0), reverse=True)[:3]
        TopThreads     = sorted(Data, key=lambda x: x.get("threads", 0),        reverse=True)[:3]
        TopOpenFiles   = [d for d in Data if isinstance(d.get("open_files"), int)]
        TopOpenFiles   = sorted(TopOpenFiles, key=lambda x: x.get("open_files", 0), reverse=True)[:3]

        Summary  = "Total Processes : %d\n\n" % TotalProcesses
        Summary += "Top CPU Processes:\n"
        for p in TopCPU:
            Summary += "  %s (PID %s) - %.2f%%\n" % (p["name"], p["pid"], p["cpu_percent"])
        Summary += "\nTop Memory Processes:\n"
        for p in TopMemory:
            Summary += "  %s (PID %s) - %.2f%%\n" % (p["name"], p["pid"], p["memory_percent"])
        Summary += "\nTop Thread Count Processes:\n"
        for p in TopThreads:
            Summary += "  %s (PID %s) - %s threads\n" % (p["name"], p["pid"], p.get("threads", "N/A"))
        Summary += "\nTop Open Files Processes:\n"
        for p in TopOpenFiles:
            Summary += "  %s (PID %s) - %s files\n" % (p["name"], p["pid"], p["open_files"])

        msg = MIMEMultipart()
        msg["From"]    = SenderMail
        msg["To"]      = ReceiverMail
        msg["Subject"] = "Platform Surveillance Report - " + time.strftime("%Y-%m-%d %H:%M:%S")
        msg.attach(MIMEText(Summary, "plain"))

        with open(LogFile, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", "attachment; filename=" + os.path.basename(LogFile))
            msg.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SenderMail, SenderPassword)
        server.sendmail(SenderMail, ReceiverMail, msg.as_string())
        server.quit()
        print("Email sent to : " + ReceiverMail)

    except Exception as e:
        print("Failed to send email : " + str(e))

def main():

    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance System -----")
    print(Border)

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Store information about processes")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto-logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 4):
        print("Inside projects logic")
        print("TimeInterval : ", sys.argv[1])
        print("DirectoryName : ", sys.argv[2])
        print("ReceiverMail : ",  sys.argv[3])
        
        # Apply the schedular
        schedule.every(int (sys.argv[1])).minutes.do(CreateLog, sys.argv[2], sys.argv[3])

        print("Platform Surveillance System started successfully")
        print("Directory created with name : ", sys.argv[2])
        print("Time interval int minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till abort
        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)

if __name__ == "__main__":
    main()