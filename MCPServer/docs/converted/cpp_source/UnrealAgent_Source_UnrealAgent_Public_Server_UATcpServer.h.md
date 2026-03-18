# UnrealAgent\Source\UnrealAgent\Public\Server\UATcpServer.h

## 函数

- `UATcpServer`
- `Start`
- `Stop`
- `IsRunning`
- `GetCommandRegistry`
- `OnConnectionAccepted`
- `Tick`

## 文档注释

> * TCP server that listens for incoming JSON-RPC connections.  * Runs on the game thread via FTSTicker for safe UE API access.

> Start listening on the specified address and port

> Stop the server and close all connections

> Check if the server is currently running

> Get the command registry (shared across all connections)

> Callback when a new TCP connection is accepted

> Game thread tick - process pending client data

> TCP listener instance

> Active client connections

> Ticker delegate handle for game thread processing

> Command registry shared across all connections

> Server state
