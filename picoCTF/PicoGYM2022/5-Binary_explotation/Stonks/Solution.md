### *Stonks*
This is a jump up the complexity ladder. There is two things that is good to know or google in order to get this. First, format string vulnerability and secondly the fact that X86 memory structure is little endian.
1. Download the vulnarable C code and have a peek for something that indicate trouble.
2. printf(user_buf); in this case might be convinced to print other things than just strings... Memory contents perhaps?
3. Here comes the format vulnerability into play. By feeding it a number of %x the response might be intresting. Lets try.
