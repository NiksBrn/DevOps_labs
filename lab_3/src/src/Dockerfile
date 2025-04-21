FROM alpine:3.21 AS builder

RUN apk add --no-cache g++ make cmake

WORKDIR /app

COPY . .
RUN cmake -S . -B ./build && cmake --build build 

FROM alpine:3.21

RUN adduser -D appuser
USER appuser

WORKDIR /app

COPY --from=builder /app/build/cw .

ENTRYPOINT ["./cw"]