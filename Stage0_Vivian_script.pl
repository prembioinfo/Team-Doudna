#!/usr/bin/perl
use strict;
use warnings;

my $name = 'Vivian Chu';
my $email = 'vivian.chu@uwaterloo.ca';
my $slack = 'vivianschu';
my $biostack = 'Genomics';
my $twitter = 'vivianschu';

sub hammingdist {
        my ($j, $k) = @_;
        my $difference = $j ^ $k;
        my $mismatch = $difference =~ tr/\0//c;
        print $difference
}

my $hamming_distance = hammingdist($slack,$twitter);

my $info = <<"END";
$name, $email, \@$slack, $biostack, \@$twitter, $hamming_distance
END

print $info

#Program_using_Perl
