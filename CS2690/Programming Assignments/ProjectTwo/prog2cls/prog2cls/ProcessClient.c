// Implement ProcesClient()in a separate source code file
//named ProcessClient.c.

// Declare ProcessClient() in WSEchoServerv6.c,
//outside of main(), the same way that DisplayFatalError() is declared.Check for
//errors in the Sockets receive process, as indicated by a negative return value from
//recv().

//11. Echo the message back to the client from within ProcessClient().Be sure that all of
//the client’s message has been received and echoed by the server.You can’t count bytes
//as you did with the client, because the server doesn’t know in advance how many bytes
//to expect from the client, and whether all of those bytes will be received in the initial call
//to recv().So call recv() repeatedly until recv() returns message length 0,
//indicating that the client has closed the connection. (See the Lecture 11 slide titled
//	“recv()” for details.)
// 

//	12. While still in ProcessClient(), close the client socket, return to the “forever” loop in
//	WSEchoServerv6.c, then call accept() and wait for another client connection.