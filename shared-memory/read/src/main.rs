use shared_memory::{ShmemConf, ShmemError};
use memmap::MmapOptions;
use std::fs::File;
use std::io::Read;
use std::io::Write;
use std::fs::OpenOptions;
use memmap::Mmap;
use memmap::MmapMut;
// use memmap2::Mmap;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let file_path = "shared_memory.bin";
    let data_to_write = "Hello, this is shared memory data!\n";

    // Open the shared memory file in write mode
    let file = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .open(file_path)?;

    // Truncate the file to the size of the data to be written
    file.set_len(data_to_write.len() as u64)?;

    // Memory map the file
    let mut mapped_file = unsafe { MmapMut::map_mut(&file)? };

    // Write the data to the memory map
    mapped_file.write(data_to_write.as_bytes())?;
    
    let shared_memory_name = "my_large_data";
    // Create or open the shared memory mapping
    // let shmem = match ShmemConf::new().flink(shmem_flink).open() {
    //     Ok(m) => m,
    //     Err(e) => {
    //         panic!("Unable to create or open shmem flink {shmem_flink} : {e}");
    //     }
    // };
    let file = OpenOptions::new()
    .read(true)
    .open("shared_memory.bin")?;

    // Memory map the file
    let mapped_file = unsafe { Mmap::map(&file)? };

    // Read the data from the memory map
    let data = &mapped_file[..];
    println!("data: {:?}", data);
    // let file = File::open("my_large_data")?;
    // let mmap = unsafe { MmapOptions::new().map(&file)? };
    // assert_eq!(b"# memmap2", &mmap[0..9]);
    
    // let mut file = File::open(shared_memory_name)?;

    // let mut contents = Vec::new();
    // file.read_to_end(&mut contents)?;

    // let mmap = unsafe { Mmap::map(&file)?  };

    // assert_eq!(&contents[..], &mmap[..]);
    
    // let start = std::time::Instant::now();

    // // Read the data from the memory-mapped file into a Vec<u8>
    // // let data: Vec<u8> = mmapped_file.iter().copied().collect();


    // // Read the data from the memory-mapped file
    // // let data: Vec<u8> = mmapped_file.iter().copied().collect();
    // // assert_eq!(shared_memory[2000], 5u8);

    // println!(
    //     "Successfully got \"my_large_data\" of size {}, that took {:?}",
    //     contents.len(),
    //     start.elapsed(),
    // );


    // Get pointer to the shared memory
    // unsafe {
    //     let raw_ptr = shmem.as_slice();
    //     // assert_eq!(raw_ptr[2000], 5u8);
    // }
    // let mut large_data: Vec<u8> = Vec::new();
    


    Ok(())
}
