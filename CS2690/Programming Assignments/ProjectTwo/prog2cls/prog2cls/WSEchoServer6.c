//The primary source code file will be named WSEchoServerv6.c.This will contain your
//main() function.

//Verify the correct number of command line arguments have been provided by the user.
//If no port number is included on the command line, you may use a default port of your own choosing.

//2. Initialize the WinSock DLL.After a successful call to WSAStartup(), handle any errors by
//calling DisplayFatalErr().

//3. Create the server socket.

//4. Load the server information into the server’s sockaddr_in6 structure(see Lecture 12
//	slide titled “Server Socket Initialization”).Use in6addr_any as the server’s IP
//	address.

//	5. bind() the server socket to this sockaddr_in6 structure.

//	6. Call listen() to tell the server the maximum simultaneous client connection requests
//	to allow.

//	7. Display a message on the server console that includes your initials, similar to this:
//JD's IPv6 echo server is ready for client connection...

//8. Enter a “forever” loop like this :
//	for (;;) { ... }

//From within this loop, call accept() and wait for a client connection.
//Echo back one complete client message per connection request. 

//	9. Each time a client connects to the server in this loop, display the IP address and port
//	number of the client, and the server’s own port number(from the server’s
//		sockaddr_in6) on the server’s console

//Use inet_ntop() to convert an IP address from network format into a text string
//suitable for display(as shown above).Use ntohs() to convert a 16 - bit port number
//from network format back into a 16 - bit Windows integer.Verify that both port numbers
//are displayed as numerically correct values(not reversed).

//10. From within the “forever” loop, call a function named ProcesClient() to receive the
//message from your client.




//	13. While waiting in the “forever” loop for client communication, the server can be terminated
//	with CTRL + C.No special programming is required to enable this.Note that CTRL + C
//	works when running the server from the command line, but not if you are running it in the
//	Visual Studio debugger.Because we are using this crude termination mechanism for the
//	server, no call to closesocket() will be needed to close the server socket and no call
//	to WSACleanup() will be needed to release the WinSock DLL resources.Those
//	functions will be handled by the operating system. (In a real sockets program, omitting
//		closesocket() and WSACleanup() would be considered poor design.)