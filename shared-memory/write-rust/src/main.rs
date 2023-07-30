extern crate memmap2;

use std::{
    fs::OpenOptions,
    io::{Seek, SeekFrom, Write},
};
use memmap2::Mmap;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut large_data = vec![u8::default(); 49_152_000 * 4];
    large_data[2000] = 5u8;

    let mut f = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .open("/tmp/test.mmap")?;

    let start = std::time::Instant::now();
    // Allocate space in the file first
    f.seek(SeekFrom::Start((large_data.len() - 1).try_into()?))?;
    f.write_all(&[0])?;
    f.seek(SeekFrom::Start(0))?;

    let mut mmap = unsafe { Mmap::map(&f)?.make_mut()? };

    mmap.copy_from_slice(&large_data);
    // mmap[2000] = 5u8;
    println!(
        "Successfully write \"my_large_data\" of size {}, that took {:?}",
        large_data.len(),
        start.elapsed(),
    );


    Ok(())
}
