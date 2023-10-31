
#include <winsock2.h>
#include <stdio.h>

void ProcessClient(SOCKET clientSocket) {
    char buffer[1024];
    int bytesRead;

    do {
        bytesRead = recv(clientSocket, buffer, sizeof(buffer), 0);

        if (bytesRead < 0) {
            DisplayFatalErr("Error reading from client.\n");
            break;
        }
        else if (bytesRead == 0) {
            break; 
        }
        else {
            send(clientSocket, buffer, bytesRead, 0);
        }
    } while (bytesRead > 0);

    closesocket(clientSocket);
}
