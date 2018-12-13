""""
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>

int main(void)
{
  int listenfd = 0,connfd = 0;

  struct sockaddr_in serv_addr;

  char sendBuff[1025];
  int numrv;

  listenfd = socket(AF_INET, SOCK_STREAM, 0);
  printf("socket retrieve success\n");

  memset(&serv_addr, '0', sizeof(serv_addr));
  memset(sendBuff, '0', sizeof(sendBuff));

  serv_addr.sin_family = AF_INET;
  serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
  serv_addr.sin_port = htons(5000);

  bind(listenfd, (struct sockaddr*)&serv_addr,sizeof(serv_addr));

  if(listen(listenfd, 10) == -1){
      printf("Failed to listen\n");
      return -1;
  }

  while(1)
    {

      connfd = accept(listenfd, (struct sockaddr*)NULL ,NULL); // accept awaiting request

      strcpy(sendBuff, "This is Arnab Calling From Space!!");
      write(connfd, sendBuff, strlen(sendBuff));

      close(connfd);
      sleep(1);
    }

  return 0;
}
"""

import socket

if __name__=="__main__":
    """Create a TCP/IP server that listens on port 23000 on localhost
    read the data received, and print it;
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('', 23000))
    # a hint to os, that connections more than 5 may be dropped
    server_sock.listen(5)
    # Creates client to show you what you have sent
    while True:
        client_sock, (remote_host, remote_port) = server_sock.accept()
        string_received = client_sock.recv(100)
        client_sock.send(string_received)
        print("s", string_received)
        client_sock.close()

