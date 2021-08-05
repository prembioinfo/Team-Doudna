#!/usr/bin/perl
use strict;
use warnings;

my $name = 'Vivian Chu';
my $email = 'vivian.chu@uwaterloo.ca';
my $slack = 'vivianschu';
my $biostack = 'Genomics';
my $twitter = 'vivianschu';

sub hd {
        my ($k, $l) = @_;
        my $diff = $k ^ $l;
        my $num_mismatch = $diff =~ tr/\0//c;
        print $diff
}

my $hamming_distance = hd($slack,$twitter);

my $info = <<"END";
$name, $email, \@$slack, $biostack, \@$twitter, $hamming_distance
END

print $info

#Program_using_Perl
