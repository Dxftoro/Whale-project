FROM gcc:latest AS build

#RUN apt-get update && apt-get install -y git
#RUN git clone https://github.com/Dxftoro/Lnshell-nerfed.git /src/

WORKDIR /src/
COPY ./ctest/ /src/
RUN gcc -o output ./*.c

FROM alpine:latest AS final
RUN apk add gcompat

WORKDIR /app/
COPY --from=build /src/output /app/
RUN chmod +x /app/output

CMD ["./output"]
