#include <stdio.h>
#include <windows.h>

int main(VOID) {
	STARTUPINFO si;
	PROCES_INFORMATION pi;

	ZeroMemory(&si, sizeof(si));
	si.cb = sizeof(si);
	zeroMemory(&pi, sizeof(pi));

	if (!CreateProcess(NULL, "C:\\WINDOWS\\system32\\mspaint.exe",
		NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi)) {
		fprint(stderr, "Create Process Failed");
		return -1;
	}


	WaitForSingleObject(pi.hProcess, INFINITE);
	printf("Child Complete");

	CloseHandle(pi.hProcess);
	CloseHandle(pi.hThread);