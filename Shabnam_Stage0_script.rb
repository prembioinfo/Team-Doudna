#Hackbio_Stage0_My_Details_

Name="Shabnam S";
Email_id="shab31201@gmail.com";
Slack_username="@Shabnam";
Twitter_username="@Shabs3s";
Biostack="Genomics";
puts "Name: #{Name}\nEmail id: #{Email_id}\nSlack Username: #{Slack_username}\nTwitter username: #{Twitter_username}\nBiostack: #{Biostack}";
def hamming(string1,string2)
     str1=string1.downcase.split('')
     str2=string2.downcase.split('')
     hamming_count=0

    str1.each_index do |i| 
        hamming_count +=1 if str1.values_at(i)!=str2.values_at(i)
    end
    hamming_count

end

a=hamming("#{Slack_username}","#{Twitter_username}")
puts "Hamming Distance = #{a}"
#Program_using_ruby
