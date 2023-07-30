use std::io::Read;
use std::io::BufReader;
use std::fs::File;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let f = File::open("/shared_data/data.txt")?;
    let mut reader = BufReader::new(f);
    let mut large_data: Vec<u8> = Vec::new();
    
    let start = std::time::Instant::now();
    reader.read_to_end(&mut large_data)?;
    assert_eq!(large_data[2000], 5u8);
    println!(
        "Successfully got \"my_large_data\" of size {}, that took {:?}",
        large_data.len(),
        start.elapsed(),
    );

    Ok(())
}
