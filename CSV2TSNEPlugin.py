import sys
import PyPluMA

class CSV2TSNEPlugin:
    def input(self, filename):
       self.parameters = dict()
       paramfile = open(filename, 'r')
       for line in paramfile:
         self.contents = line.split('\t')
         self.parameters[self.contents[0]] = self.contents[1].strip()

       self.csvfile = open(PyPluMA.prefix()+"/"+self.parameters["csvfile"], 'r')
       self.metafile = open(PyPluMA.prefix()+"/"+self.parameters["metafile"], 'r')

    def run(self):
       self.header = self.csvfile.readline().strip()
       if (self.header.startswith('\"\",')):
           self.header = self.header[3:]
       self.header = self.header.replace('(', '').replace(')', '').replace(' ', '').replace('[', '').replace(']', '').replace('.','').replace('-','').replace('_','').replace('/','').replace('\'','').replace('=','').replace(':','').replace('*','')
       self.contents = self.header.split(',')
       #if (self.contents[0] == '\"\"'):
       #    self.contents.remove('\"\"')

       for i in range(len(self.contents)):
           if (self.contents[i][0] == '\"'):
               self.contents[i] = self.contents[i][1:len(self.contents[i])-1]

       self.header2 = self.metafile.readline().strip()
       self.contents2 = self.header2.split(',')
       self.sample_idx = self.contents2.index('\"Sample\"')
       self.group_idx =self.contents2.index('\"Group\"')


    def output(self, prefix):
       catfile = open(prefix+".catfiles.txt", 'w')
       featurefile = open(prefix+".features.txt", 'w')
       datafile = open(prefix+".data.csv", 'w')
       groups = dict()

       for line in self.metafile:
          self.contents3 = line.strip().split(',')
          for i in range(len(self.contents3)):
             if (self.contents3[i][0] == '\"'):
               self.contents3[i] = self.contents3[i][1:len(self.contents3[i])-1]
          if (self.contents3[self.group_idx] in groups):
              groups[self.contents3[self.group_idx]].append(self.contents3[self.sample_idx])
          else:
              groups[self.contents3[self.group_idx]] = [self.contents3[self.sample_idx]]

       for group in groups:
          outfilename = prefix+"."+group+".txt"
          catfile.write(group+"\t"+outfilename+"\n")
          outfile = open(outfilename, 'w')
          for sample in groups[group]:
              outfile.write(sample+"\n")

       for feature in self.contents:
          featurefile.write(feature+"\n")

       datafile.write(self.header+"\n")
       for line in self.csvfile:
           datafile.write(line)
