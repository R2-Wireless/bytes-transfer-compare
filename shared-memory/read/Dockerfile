FROM rust:1.68.0-slim-buster as builder
WORKDIR /build
COPY ./Cargo.toml ./Cargo.lock ./
RUN echo 'fn main() { println!("Is dummy"); }' > ./dummy.rs && \
    sed -i 's|"src/main.rs"|"dummy.rs" # 1|' Cargo.toml && \
    CARGO_REGISTRIES_CRATES_IO_PROTOCOL=sparse cargo build --release && \
    rm ./dummy.rs && \
    sed -i 's|"dummy.rs" # 1|"src/main.rs"|' Cargo.toml
COPY ./src ./src
RUN CARGO_REGISTRIES_CRATES_IO_PROTOCOL=sparse cargo build --release

FROM scratch as runtime

WORKDIR /app
COPY --from=builder /build/target/release/main .

ENTRYPOINT [ "/bin/bash", "-c", "/app/$0 $" ] 
CMD [ "main" ]
