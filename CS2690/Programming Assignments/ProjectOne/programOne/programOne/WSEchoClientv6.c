//// CS 2690 Program 1 
//// Simple Windows Sockets Echo Client (IPv6)
//// Last update: 2/12/19
//// <Your name here> <Your section here> <Date>
//// <Your Windows version and Visual Studio version>
////
//// Usage: WSEchoClientv6 <server IPv6 address> <server port> <"message to echo">
//// Companion server is WSEchoServerv6
//// Server usage: WSEchoServerv6 <server port>
////
//// This program is coded in conventional C programming style, with the 
//// exception of the C++ style comments.
////
//// I declare that the following source code was written by me or provided
//// by the instructor. I understand that copying source code from any other 
//// source or posting solutions to programming assignments (code) on public
//// Internet sites constitutes cheating, and that I will receive a zero 
//// on this project if I violate this policy.
//// ----------------------------------------------------------------------------
//
//// Minimum required header files for C Winsock program
//#include <stdio.h>       // for print functions
//#include <stdlib.h>      // for exit() 
//#include <winsock2.h>	 // for Winsock2 functions
//#include <ws2tcpip.h>    // adds support for getaddrinfo & getnameinfo for v4+6 name resolution
//#include <Ws2ipdef.h>    // optional - needed for MS IP Helper
//
//// #define ALL required constants HERE, not inline 
//// #define is a macro, don't terminate with ';'  For example...
//#define RCVBUFSIZ 50
//
//// declare any functions located in other .c files here
//void DisplayFatalErr(char* errMsg); // writes error message before abnormal termination
//
//void main(int argc, char* argv[])   // argc is # of strings following command, argv[] is array of ptrs to the strings
//{
//	// Declare ALL variables and structures for main() HERE, NOT INLINE (including the following...)
//	WSADATA wsaData;                // contains details about WinSock DLL implementation
//	struct sockaddr_in6 serverInfo = { 0 };	// standard IPv6 structure that holds server socket info
//
//	// Verify correct number of command line arguments, else do the following:
//	if (argc != 4) {
//		fprintf(stderr, "Expected parameters: <server IPv6 addr> <server port> <\"Msg to echo\">\n");
//		exit(1); // ...and terminate with abnormal termination code(1)
//	}
//
//
//	// Retrieve the command line arguments. (Sanity checks not required, but port and IP addr will need
//	// to be converted from char to int.  See slides 11-15 & 12-3 for details.)
//	char* serverIPaddr = argv[1];
//	int serverPort = atoi(argv[2]);
//
//
//	// Initialize Winsock 2.0 DLL. Returns 0 if ok. If this fails, fprint error message to stderr as above & exit(1).  
//	if (WSAStartup(MAKEWORD(2,0), &wsaData) != S_OK) {
//		fprintf(stderr, "Unable to load WinSock API. Go pound sand.\n");
//		exit(2); // ...and terminate with abnormal termination coude (2)
//	}
//
//	int sock;
//	sock = (int) socket(AF_INET6, SOCK_STREAM, IPPROTO_TCP);
//
//	if (sock == INVALID_SOCKET) {
//		DisplayFatalErr("Unable to 'create' a client socket.\n");
//	}
//
//	// Load server info into sockaddr_in6 
//	serverInfo.sin6_family = AF_INET6;         // address family = IPv6
//	serverInfo.sin6_port = htons(serverPort);  // convert int port to ntwk order*
//
//	// Convert cmd line server addr from char to ntwk form, load into sockaddr_in6 
//	inet_pton(AF_INET6, serverIPaddr, &serverInfo.sin6_addr);
//
//	// The DisplayFatalErr() function uses info from lpWSAData, so don’t 
//	// call it until after the Winsock DLL is loaded.
//
//	// Display helpful confirmation messages after key socket calls like this:
//	// printf("Socket created successfully.  Press any key to continue...");
//	// getchar();     // needed to hold console screen open
//
//	// If doing extra credit IPv4 address handling option, add the setsockopt() call as follows...
//	// if (perrno = setsockopt(sock, IPROTO_IPV6, IPV6_V6ONLY, (char *)&v6Only, sizeof(v6Only)) != 0)
//	//     DisplayFatalErr("setsockopt() function failed.");  
//
//	// Zero out the sockaddr_in6 structure and load server info into it.  See slide 11-15.
//	// Don't forget any necessary format conversions.
//
//	// Attempt connection to the server.  If it fails, call DisplayFatalErr() with appropriate message,
//	// otherwise printf() confirmation message
//
//	if (connect(sock, (struct sockaddr*)&serverInfo, sizeof(serverInfo)) < 0) {
//		DisplayFatalErr("connect() function failed.");
//	}
//
//	// Send message to server (without '\0' null terminator). Check for null msg (length=0) & verify all bytes were sent...
//	char* msg = argv[3];
//	int msgLen = strlen(msg);
//	// ...else call DisplayFatalErr() with appropriate message as before
//	
//	int index = 0;
//	do
//	{
//		int bytesSent = send(sock, &msg[index], msg - index, 0);
//		if (bytesSent == SOCKET_ERROR)
//		{
//			DisplayFatalErr("send() function failed");
//		}
//		else {
//			index += bytesSent;
//		}
//	} while (index < msgLen);
//
//
//	// Retrieve the message returned by server.  Be sure you've read the whole thing (could be multiple segments). 
//	unsigned char recvBuffer[RCVBUFSIZ] = { 0 };
//	index = 0;
//
//	// Manage receive buffer to prevent overflow with a big message.
//	// Call DisplayFatalErr() if this fails.  (Lots can go wrong here, see slides.)
//	do
//	{
//		int bytesReceived = recv(sock, &msg[index], RCVBUFSIZ - index, 0);
//		if (bytesReceived == SOCKET_ERROR)
//		{
//			DisplayFatalErr("recv() function failed");
//		}
//		else if (bytesReceived == 0) 
//		{
//			break;
//		}
//		else 
//		{
//			index += bytesReceived;
//			recvBuffer[bytesReceived] = 0;
//			printf("%s", recvBuffer);
//		}
//	} while (index < msgLen);
//
//
//
//	// Display ALL of the received message, in printable C string format.
//
//	// Close the TCP connection (send a FIN) & print appropriate message.
//
//	// Release the Winsock DLL
//
//	fprintf(stderr, "Connection established with server. Press any key to continue.");
//	getchar();
//
//	exit(0);
//}
