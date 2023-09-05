# Gumball Machine with Proxy Pattern
Note:  java PATH and CLASSPATH need to be set

To get code running on localhost: 

1. Change directories to level: homedir/gumball/GumballMachineTestDrive

2. Run rmiregistry in background:
    Linux:
    rmiregistry &

    windows 10:
    start rmiregistry

3. Run:
java gumball.GumballMachineTestDrive localhost 300

4. In a different window, run:
java gumball.GumballMonitorTestDrive localhost




