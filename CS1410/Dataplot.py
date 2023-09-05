import matplotlib.pyplot as plt
import numpy as np
import glob


def analyze(fname):
    rawArray = np.loadtxt(fname)
    smoothArray = rawArray.copy()
    for i in range(3, len(rawArray)-3):
        b = ((rawArray[i-3]) + (2*rawArray[i-2]) + (3*rawArray[i-1]) + (3*rawArray[i]) + (3*rawArray[i+1]) +
             (2*rawArray[i+2]) + (rawArray[i+3]))//15
        smoothArray[i] = b

    i = 0
    pulseList = []
    test = True
    while i < (len(smoothArray)-2):
        if (smoothArray[i+2] - smoothArray[i]) > 100 and test:
            pulseList.append(i)
            i += 1
            test = False
        if (smoothArray[i+2] - smoothArray[i]) < 0:
            test = True
        i += 1

    '''Creates new file with .out file type and opens as f'''
    file = fname[:-3]+"out"
    f = open(file, "a")
    f.write(fname + ":")
    '''
        For loop loops the length of pulseList. 
        Try statement calls function that returns the pulse area for all pulses except for the last pulse
        Except statement call function that returns the pulse area for the last pulse.
    '''
    for i in range(len(pulseList)):
        try:
            h = area(pulseList[i], rawArray, pulseList[i + 1])
            # Prints the start pulse and pulse area to .out file
            f.write("\nPulse {}: {} ({})".format((i+1), pulseList[i]+1, h))

        except:
            h = psLast(pulseList[i], rawArray)
            # Prints the start pulse and pulse area to .out file
            f.write("\nPulse {}: {} ({})".format((i + 1), pulseList[i]+1, h))

    pdf = fname[:-3] + "pdf"
    fig, axis = plt.subplots(nrows=2)
    axis[0].plot(rawArray)
    axis[0].set(title=fname, yLabel="raw")
    axis[1].plot(smoothArray)
    axis[1].set(yLabel="smooth")
    fig.savefig(pdf)


def area(currentPulse, a, nextPulse):
    '''
        If statement for two separate conditions:
        The first condition is if there is a difference of 50 or more locations between the current and next pulse
        The second condition is if the next pulse is within 50 locations of the current pulse
    '''

    pulsearea = 0
    value = nextPulse - currentPulse
    if value > 50:
        for i in range(currentPulse, currentPulse + 50):
            pulsearea += a[i]
    else:
        for i in range(currentPulse, nextPulse):
            pulsearea += a[i]
    return pulsearea


def psLast(pstart1, a):
    '''Since this is the last pulse we simply loop through the next 50 pulse after the current pulse.'''
    pulsearea = 0
    for i in range(pstart1, pstart1 + 50):
        pulsearea += a[i]
    return pulsearea


def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)


if __name__ == "__main__":
    main()