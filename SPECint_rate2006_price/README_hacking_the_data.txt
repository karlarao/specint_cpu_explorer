hacking the data (also visit cpu - power - SPECpower_ssj2008 http://bit.ly/2giK21T)

-- cpuprice.txt
go to http://www.cpu-world.com/Price_Compare/Server_CPU_prices_(latest).html and copy contents
vi price.txt, then replace $ with USD
cat price.txt | grep " USD" > cpuprice.txt
sed -i '' 's/- USD/,/g' cpuprice.txt
sed -i '' 's/Xeon/Intel Xeon/g' cpuprice.txt
sed -i '' 's/Opteron/AMD Opteron/g' cpuprice.txt
sed -i '' 's/ //g' cpuprice.txt

-- spec.txt
cat spec.csv | awk -F , '{print $8","$0}' > spec.txt
sed -i '' 's/ //g' spec.txt

./compare.py -f cpuprice.txt -t spec.txt > specprice.txt

vi specprice.txt, then update the header with price

Processor,Benchmark,"HardwareVendor     ",System,#Cores,#Chips,#CoresPerChip,#ThreadsPerCore,Processor,ProcessorMHz,ProcessorCharacteristics,CPU(s)Orderable,AutoParallelization,BasePointerSize,PeakPointerSize,1stLevelCache,2ndLevelCache,3rdLevelCache,OtherCache,Memory,OperatingSystem,FileSystem,Compiler,HWAvail,SWAvail,BaseCopies,Result,Baseline,400Peak,400Base,401Peak,401Base,403Peak,403Base,429Peak,429Base,445Peak,445Base,456Peak,456Base,458Peak,458Base,462Peak,462Base,464Peak,464Base,471Peak,471Base,473Peak,473Base,483Peak,483Base,License,TestedBy,TestSponsor,TestDate,Published,Updated,Price

LANG=C sed -i '' 's/Jan-/01\/01\//g' specprice.txt
LANG=C sed -i '' 's/Feb-/02\/01\//g' specprice.txt
LANG=C sed -i '' 's/Mar-/03\/01\//g' specprice.txt
LANG=C sed -i '' 's/Apr-/04\/01\//g' specprice.txt
LANG=C sed -i '' 's/May-/05\/01\//g' specprice.txt
LANG=C sed -i '' 's/Jun-/06\/01\//g' specprice.txt
LANG=C sed -i '' 's/Jul-/07\/01\//g' specprice.txt
LANG=C sed -i '' 's/Aug-/08\/01\//g' specprice.txt
LANG=C sed -i '' 's/Sep-/09\/01\//g' specprice.txt
LANG=C sed -i '' 's/Oct-/10\/01\//g' specprice.txt
LANG=C sed -i '' 's/Nov-/11\/01\//g' specprice.txt
LANG=C sed -i '' 's/Dec-/12\/01\//g' specprice.txt

