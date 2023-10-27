//The primary source code file will be named WSEchoServerv6.c.This will contain your
//main() function.
// Minimum required header files for C Winsock program
#include <stdio.h>       // for print functions
#include <stdlib.h>      // for exit() 
#include <winsock2.h>	 // for Winsock2 functions
#include <ws2tcpip.h>    // adds support for getaddrinfo & getnameinfo for v4+6 name resolution
#include <Ws2ipdef.h>    // optional - needed for MS IP Helper
void main(int argc, char* argv[]) {

	char* serverIPaddr;
	int serverPort = 0;

	// Declare ALL variables and structures for main() HERE, NOT INLINE (including the following...)
	WSADATA wsaData;                // contains details about WinSock DLL implementation
	struct sockaddr_in6 serverInfo = { 0 };	// standard IPv6 structure that holds server socket info

	//Verify the correct number of command line arguments have been provided by the user.
	//If no port number is included on the command line, you may use a default port of your own choosing.
	if (argc == 2) {
		serverIPaddr = argv[1];
		serverPort = 5000;
		



	}
	else if (argc == 3) {
		serverIPaddr = argv[1];
		int serverPort = atoi(argv[2]);
	}
	else {
		fprintf(stderr, "Expected parameters: <server IPv6 addr> <server port> <\"Msg to echo\">\n");
		exit(1); // ...and terminate with abnormal termination code(1)
	}

	//2. Initialize the WinSock DLL.After a successful call to WSAStartup(), handle any errors by
	//calling DisplayFatalErr().
	if (WSAStartup(MAKEWORD(2, 0), &wsaData) != S_OK) {
		fprintf(stderr, "Unable to load WinSock API. Go pound sand.\n");
		exit(2); // ...and terminate with abnormal termination coude (2)
	}

	//3. Create the server socket.
	int sock;
	sock = (int) socket(AF_INET6, SOCK_STREAM, IPPROTO_TCP);

	//4. Load the server information into the server’s sockaddr_in6 structure(see Lecture 12
	//	slide titled “Server Socket Initialization”).Use in6addr_any as the server’s IP
	//	address.
	serverInfo.sin6_family = AF_INET6;         // address family = IPv6
	serverInfo.sin6_port = htons(serverPort);  // convert local port to big endian
	serverInfo.sin6_addr = in6addr_any;

	//	5. bind() the server socket to this sockaddr_in6 structure.
	bind(sock, (struct sockaddr_in6*)&serverInfo, sizeof(serverInfo));


	//	6. Call listen() to tell the server the maximum simultaneous client connection requests
	//	to allow.
	listen(sock, SOMAXCONN);

	//	7. Display a message on the server console that includes your initials, similar to this:
//JD's IPv6 echo server is ready for client connection...
	fprintf(stderr,"CS's IPv6 echo server is ready for client connection...\n");

	//8. Enter a “forever” loop like this :
//	for (;;) { ... }
//From within this loop, call accept() and wait for a client connection.
//Echo back one complete client message per connection request. 
	int client_soc;
	for (;;) {
		client_soc = accept(sock, (struct sockaddr_in6*)&serverInfo, sizeof(serverInfo));

		if (client_soc < 0) {
			fprintf(stderr, "Error accepting connection");
			continue;
		}

		//	9. Each time a client connects to the server in this loop, display the IP address and port
		//	number of the client, and the server’s own port number(from the server’s
		//		sockaddr_in6) on the server’s console
		//Use inet_ntop() to convert an IP address from network format into a text string
		//suitable for display(as shown above).Use ntohs() to convert a 16 - bit port number
		//from network format back into a 16 - bit Windows integer.Verify that both port numbers
		//are displayed as numerically correct values(not reversed).
		char str[INET6_ADDRSTRLEN];
		fprintf(stderr,"Server port: %d connection accepted from client IP: %s on port %d\n", serverPort, inet_ntop(AF_INET6,&serverInfo,str,INET6_ADDRSTRLEN), ntohs(serverInfo.sin6_port));

		//10. From within the “forever” loop, call a function named ProcesClient() to receive the
		//message from your client.


	}
}











//	13. While waiting in the “forever” loop for client communication, the server can be terminated
//	with CTRL + C.No special programming is required to enable this.Note that CTRL + C
//	works when running the server from the command line, but not if you are running it in the
//	Visual Studio debugger.Because we are using this crude termination mechanism for the
//	server, no call to closesocket() will be needed to close the server socket and no call
//	to WSACleanup() will be needed to release the WinSock DLL resources.Those
//	functions will be handled by the operating system. (In a real sockets program, omitting
//		closesocket() and WSACleanup() would be considered poor design.)
