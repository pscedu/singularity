#sort repositories
file = open("README.md", "w")

# STEM
repositories = ['star-fusion','filtlong','porechop','anvio','funannotate','fastq-tools','meme-suite','braker2','rust','guppy','guppy-gpu','bsmap','salmon','rnaview','bioformats2raw','raw2ometiff','flash','blat','bedops','genemark-es','augustus','checkm','ncview','bowtie2','asciigenome','fastqc','sra-toolkit','gatk','hmmer','bcftools','raxml','spades','busco','samtools','bedtools','bamtools','fastani','phylip-suite','blast','viennarna','cutadapt','bismark','star','prodigal','bwa','picard','hisat2','abyss','octave','tiger','gent','methylpy','fasttree','vcf2maf','htslib','kraken2','aspera-connect','trimmomatic']
repositories.sort()
file.write('# List of Singularity definition files, modulefiles and more\n')
file.write('[![Build it!](https://github.com/pscedu/singularity/actions/workflows/build.yml/badge.svg)](https://github.com/pscedu/singularity/actions/workflows/build.yml)\n')
file.write('[![](https://imgs.xkcd.com/comics/code_quality.png)](https://xkcd.com/1513/)\n\n')
file.write('This repository lists the Singularity definition files and other files needed to deploy software on Bridges2, HuBMAP HIVE and Brain Image Library.\n')
file.write('## STEM\n')
file.write( '| Name | Information |\n' )
file.write( '| --- | --- |\n' )

for repository in repositories:
  str = '| [' + repository + '](http://github.com/pscedu/singularity-' + repository + ') | ![Status](https://github.com/pscedu/singularity-' + repository + '/actions/workflows/main.yml/badge.svg)![Status](https://github.com/pscedu/singularity-' + repository + '/actions/workflows/pretty.yml/badge.svg)![Issue](https://img.shields.io/github/issues/pscedu/singularity-' + repository + ')![forks](https://img.shields.io/github/forks/pscedu/singularity-' + repository + ')![Stars](https://img.shields.io/github/stars/pscedu/singularity-' + repository + ')![License](https://img.shields.io/github/license/pscedu/singularity-' + repository + ') |\n'
  file.write( str )

# Utilities
repositories = ['hashdeep','dua','vim','libtiff-tools','wordgrinder','shellcheck','pandiff','rich-cli','jq','jp','lowcharts','btop','aws-cli','cwltool','circos','glances','fdupes','graphviz','browsh','hyperfine','dust','gnuplot','pandoc','mc','bat','flac','visidata','octave','ncdu','lazygit','asciinema','ffmpeg','imagemagick','rclone']
repositories.sort()
file.write('\n## Utilities\n')
file.write( '| Name | Information |\n' )
file.write( '| --- | --- |\n' )

for repository in repositories:
  str = '| [' + repository + '](http://github.com/pscedu/singularity-' + repository + ') | ![Status](https://github.com/pscedu/singularity-' + repository + '/actions/workflows/main.yml/badge.svg)![Status](https://github.com/pscedu/singularity-' + repository + '/actions/workflows/pretty.yml/badge.svg)![Issue](https://img.shields.io/github/issues/pscedu/singularity-' + repository + ')![forks](https://img.shields.io/github/forks/pscedu/singularity-' + repository + ')![Stars](https://img.shields.io/github/stars/pscedu/singularity-' + repository + ')![License](https://img.shields.io/github/license/pscedu/singularity-' + repository + ') |\n'
  file.write( str )

file.write('---\nCopyright © 2020-2024 Pittsburgh Supercomputing Center. All Rights Reserved.\n\nThe [Biomedical Applications Group](https://www.psc.edu/biomedical-applications/) at the [Pittsburgh Supercomputing Center](http://www.psc.edu) in the [Mellon College of Science](https://www.cmu.edu/mcs/) at [Carnegie Mellon University](http://www.cmu.edu).')
file.close()
