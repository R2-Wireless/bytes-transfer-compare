FROM rust:1.68.0-slim as builder
WORKDIR /build
ARG TARGETARCH
RUN if [ "$TARGETARCH" = "arm64" ]; then \
        echo "aarch64-unknown-linux-musl" > RUST_TARGET; \
    else \
        echo "x86_64-unknown-linux-musl" > RUST_TARGET; \
    fi
RUN rustup target add $(cat RUST_TARGET)
ENV CARGO_REGISTRIES_CRATES_IO_PROTOCOL sparse
COPY ./Cargo.toml ./Cargo.lock ./
RUN echo 'fn main() { println!("Is dummy"); }' > ./dummy.rs && \
    sed -i 's|"src/main.rs"|"dummy.rs" # 1|' Cargo.toml && \
    cargo build --release --locked --target $(cat RUST_TARGET) && \
    rm ./dummy.rs && \
    sed -i 's|"dummy.rs" # 1|"src/main.rs"|' Cargo.toml
COPY ./src ./src
RUN cargo build --release --locked --target $(cat RUST_TARGET)
RUN mv target/$(cat RUST_TARGET)/release/ target/main

FROM scratch as runtime
COPY --from=builder /build/target/main /bin/
CMD ["main"]
