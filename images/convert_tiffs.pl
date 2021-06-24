#!/bin/perl 
#
#
# Readme: 
#   This script currently searches for all files IN THE CURRENT WORKING DIRECTORSY  that contain the keyword (Bright) and merges them into a movie called /tmp/allKEYWORD.tiff"
#
# Note: 
# The imagemagick policy seemed to override my command line options, so I manually set the memory limit to 10 GiB in  /etc/ImageMagick-6/policy.xml 
#
use warnings; 
use strict;

#my $keyword = "Green";
my $keyword = "Bright";
my $prefix ="*$keyword*";
my $output = "/tmp/all$keyword.tiff"; 
my $maxFiles = 300;
print("Searching for $prefix\n");
my $x = `ls $prefix`;

my @files = split("\n",$x);

my $line = "";
my $ctr = 0;
foreach my $i (@files){
	#print($i);
	$line.="\"$i\" ";
	$ctr++; 
	last if $ctr>$maxFiles;
}
#my $args = "-limit memory 10xB -limit disk 100GB";
my $args = "-limit memory 10GB -limit disk unlimited";
my $sys =" convert $args ".$line;
$sys .=" $output";   
#print($sys);
print("Converting to $output\n");
system($sys );
