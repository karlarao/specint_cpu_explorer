#!/usr/bin/env python
##################################################################################################################
#  Name:        compare and append at the end of line                                                            #
#  Description: compare file A to file B, if match then append price data to file B                              #
#                                                                                                                #
#  usage:                                                                                                        #
#                                                                                                                #
#  karl [-f from_file] [-t to_file] [-v] [-h]                                                                    #
#  options:                                                                                                      #
#    -h, --help  show this help message and exit                                                                 #
#    -f          from file                                                                                       #
#    -t          to file                                                                                         #
#    -v          print version info.                                                                             #
#                                                                                                                #
##################################################################################################################

# --------------------------------------
# ---- Import Python Modules -----------
# --------------------------------------
from os.path    import basename
from sys        import exit, argv
from optparse   import OptionParser

# --------------------------------------
# ---- Main Program --------------------
# --------------------------------------
if (__name__ == '__main__'):
  Cmd            = basename(argv[0])
  Version        = '1.00'
  Banner         = Cmd + ', Release ' + Version + ' Production, Mon Mar  3 08:50:13 CST 2014'
  File1List      = []
  File2List      = []

  # Process command line options
  # ----------------------------------
  Usage  = '\n\n'
  Usage += '  ' + Cmd  + '\n'
  Usage += '  ' + Cmd  + ' -f cpuprice.txt -t spec.txt\n'
  Usage += '  ' + Cmd  + ' -h\n'
  Usage += '  ' + Cmd  + ' -v\n'

  parser = OptionParser(usage=Usage)
  parser.add_option("-f",                      dest="FromFile",   default='cpuprice.txt',     type=str, help="FromFile",           metavar='FromFile') 
  parser.add_option("-t",                      dest="ToFile",     default='spec.txt',         type=str, help="ToFile",             metavar='ToFile'  ) 
  parser.add_option("-v", action="store_true", dest="Version",    default=False,                     help="print version info."                   )
  Option, Args = parser.parse_args()

  if (Option.Version):
    print '\n' + Banner
    exit(0)

  File1 = Option.FromFile
  File2 = Option.ToFile

  try:
    FILE1 = open(File1, 'r')
  except:
    print "Cannot open " + File1 + " for read."
    exit(1)
    
  try:
    FILE2 = open(File2, 'r')
  except:
    print "Cannot open " + File2 + " for read."
    exit(1)
    
  File1Contents = FILE1.read()
  FILE1.close()
    
  File2Contents = FILE2.read()
  FILE2.close()

  for File2Line in File2Contents.split('\n'):
    # IntelXeonE5-4610,2400,37.25,12,2,6,2,428,447,Fujitsu,PRIMERGYRX500S7IntelXeonE5-46102.40GHz,8/1/2012
    if (File2Line != ''):
      if (File2Line[0] != '#'):
        if (File2Line.count(',') >= 1):
          (File2Model) = File2Line.split(',')[0]
          File2List.append((File2Model, File2Line.rstrip()))          

  # Search for Model from file1 in Model from file2 and print file2 line with price appended if found.
  for File1Line in File1Contents.split('\n'):
    # IntelXeonE5-4650L,3616
    if (File1Line != ''):
      if (File1Line[0] != '#'):
        if (File1Line.count(',') == 1):
          (File1Model, Price) = File1Line.split(',')
          for (File2Model, File2Line) in File2List:
            if File1Model == File2Model:
              print File2Line + ',' + Price
            
# --------------------------------------
# ---- End Main Program ----------------
# --------------------------------------

