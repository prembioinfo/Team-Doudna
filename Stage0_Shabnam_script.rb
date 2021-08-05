#Hackbio_Stage0_My_details

Name="Shabnam S";
Email_id="shab31201@gmail.com";
Slack_username="@Shabnam";
Twitter_username="@Shabs3s";
Biostack="Genomics";


def hamming(string1,string2)
     str1=string1.downcase.split('')
     str2=string2.downcase.split('')
     hamming_count=0
     str1.each_index do |i| 
        hamming_count +=1 if str1.values_at(i)!=str2.values_at(i)
    end
    hamming_count
end
Hamming_distance=hamming("#{Slack_username}","#{Twitter_username}")
puts "#{Name}, #{Email_id}, #{Slack_username}, #{Twitter_username}, #{Biostack}, #{Hamming_distance}"

#Program_using_ruby