extern crate memmap2;

use std::fs::OpenOptions;
use memmap2::Mmap;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let f = OpenOptions::new()
        .read(true)
        .open("/tmp/test.mmap")?;

    let mmap = unsafe { Mmap::map(&f)? };
    
    // let mut large_data = vec![u8::default(); 49_152_000];

    let start = std::time::Instant::now();
    // large_data.copy_from_slice(&mmap);

    assert_eq!(mmap[2000], 5u8);

    println!(
        "Successfully read \"my_large_data\" of size {}, that took {:?}",
        mmap.len(),
        start.elapsed(),
    );

    Ok(())
}
