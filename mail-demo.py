import os
import smtplib
import imghdr
from email.message import EmailMessage
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

emailsList = open("aa.txt", 'r')
currentEmailList = emailsList.readlines()
newcurrentEmailList=[]
for i in currentEmailList:
    i=i[:-1]
    newcurrentEmailList.append(i)
currentEmailList=newcurrentEmailList

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = currentEmailList
msg.set_content('This is a plain text email')

htmlContent = '''\
<!DOCTYPE html>
<html>
	<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
		<p style="font-size: 1.5rem; font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"><strong>Respected Sir/ Ma’am,</strong></p>
		<p>In the present lockdown situation, Shresth Legal &amp; Trademarks would like to contribute to your development and improve the worsening economic situation by <strong>Cutting Costs </strong>of our legal &amp; IP services (Trademark etc.).</p>
		<p style="font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1.2rem"><strong>WE CAN ASSIST YOU IN MATTERS OF –</strong></p>
		<p style="color: #fd7014"><strong>2. Sale / Purchase of your brand (Trademark), </strong></p>
		<p style="color: #222831"><strong>1. Trademark – Registration, Objection, Hearing, Opposition,</strong></p>
		<p style="color: #fd7014"><strong>3. Court &amp; Authorities for Drugs &amp; Cosmetics Act Cases,</strong></p>
		<p style="color: #222831"><strong>4. Drugs Control Deptt./DI/DLA for Approval/Registration of brand, </strong></p>
		<p style="color: #fd7014"><strong>5. Several Registration, Compliances before Controlling Authorities,</strong></p>
		<p style="color: #222831"><strong>6. MSME Registration- same day Certificate</strong></p>
		<hr>
		<p style="font-size: 1.05rem; font-weight:450">We are Delhi based leading law firm, operating successfully since 1997. We are managing over 6000 Trademarks serving over 100 pharma firms and over 3000 other firms, companies &amp; individuals, across the nation. We are team of Experienced Advocates, support staff, experts with over hundreds of CAs, CSs for a positive solution of the matter. <strong><br>
		<hr>
		<br>
		</strong></p>
		<table cellspacing="0" cellpadding="10" > 
			<tbody style="color:white"> 
				<tr>
					<td style="background-color: #fd7014; " colspan="3" valign="top" ><p><strong>We can serve and support you in the following court cases:</strong></p></td>
				</tr>
				<tr style="background-color: #222831;">
					<td>Civil situation</td>
					<td>Cheque Bounce</td>
					<td>Labor Law Cases</td>
				</tr>
				<tr style="background-color:#222831;">
					<td>Criminal cases</td>
					<td>Payment Recovery</td>
					<td>Banking &amp; Finance case</td>
				</tr>
				<tr style="background-color:#222831;">
					<td>Consumer Case</td>
					<td>Arbitration</td>
					<td>Contracts &amp; Agreement</td>
				</tr>
				<tr style="background-color:#222831;">
					<td>MSME</td>
					<td>ESI &amp; PF</td>
					<td>Legal notices &amp; Compl.</td>
				</tr>
			</tbody>
		</table>
		<br>
		<table border="0" cellspacing="10" cellpadding="10" style="background-color: #fd7014; color: white;" > 
			<tbody>
				<tr>
					<td valign="top" ><p><strong>Most Valuable &amp; Important Service (FOR FREE)</strong></p>
						<div>
							<br>We will be giving you regular updates for all your brands -
							<br> * If someone is Copying, infringing, Counterfeiting your mark
							<br> * Its Renewal date has approached,
							<br> Contact immediately for availing this service!
						</div>
					<br>
					</td>
				</tr>
			</tbody>
		</table>
		<br>
		<br>
		<table border="0" cellspacing="5" cellpadding="10" style="color:white"> 
			<tbody>
				<tr style="background-color:#222831;">
					<td colspan="4" valign="top" style="text-align:center"><h1>Shrestha Legal &amp; Trademarks</h1></td>
				</tr>
				<tr style="text-align:center; background-color: #fd7014; ">
					<td colspan="4" valign="top" ><h3>Outsource your Trademark </h3>
					<p>for better management</p>
					<p><strong>Get your Trademark at just Rs.1,100/- (for Indian firms)</strong></p></td>
				</tr>
				<tr style="text-align:center; background-color:#222831;">
					<td colspan="4" valign="top" ><h3>OUR TRADEMARK SERVICES (PAN INDIA) </h3>
					<p>Handling 6000+ Trademarks</p>
				</tr>
				<tr style="background-color: #fd7014; ">
					<td colspan="2" valign="top" >
						<p>Trademark, Logo Registration</p>
						<p>Objection - Reply Filing </p>
						<p>Show Cause Hearing for approval </p>
						<p>Opposition of Trademark </p>
						<p>Counter Statement Filing</p>
						<p>Infringement of Trademark</p>
						<p>Trademark Assignment</p>
						<p>Sale – Purchase of mark</p>
						<p>Renewal of Trademark Cancellation of Trademark </p>
						<p>Rectification of Trademark</p>
						<p>Change in Trademark detail</p>
						<p>Litigation of Trademark</p>
						<p>Maintenance of Trademark</p>
						<p>MSME Reg. for Trademark </p>
					</td>
					<td colspan="2" valign="top" >
						<p>Our Specialties</p>
						<p>Well Known organization</p>
						<p>Cost Effective services</p>
						<p>Transparent working </p>
						<p>Experienced legal team</p>
						<p>Hassel-free working</p>
						<p>Easy availability</p>
						<p>24 x 7 working</p>
						<p>All India Working </p>
						<p>PAN India Network</p>
						<p>Huge No. of clients </p>
						<p>Handling 6000+ marks </p>
						<p>National &amp; Intl. brands</p>
						<p>Regular Court exposure </p>
					</td>
				</tr>
				<tr style="background-color:#222831;">
					<td rowspan="3" valign="top" ><p><strong>Our Subsidized Charges for Trademarks </strong></p>
					<p><strong> (for Indian Nationals only)</strong></p></td>
					<td valign="top" ><p><strong>PLAN I</strong></p></td>
					<td valign="top" ><p><strong>PLAN II</strong></p></td>
					<td valign="top" ><p><strong>PLAN III</strong></p></td>
				</tr>
				<tr style="background-color: #fd7014; ">
					<td valign="top" >
						<p>Filing of Application</p>
						<p><strong>1,100/-</strong></p>
						<p>Filing of Reply</p>
						<p><strong>1,100/-</strong></p>
						<p>Attending Hearing</p>
						<p><strong>3,500/-</strong></p>
					</td>
					<td valign="top" >
						<p>Filing of Application</p>
						<p>+ Filing of Reply</p>
						<p><strong><s>2,700/-</s></strong></p>
						<p><strong>2,100/-</strong></p>
						<p>Attending Hearing</p>
						<p><strong>3,500/-</strong></p>
					</td>
					<td valign="top" >
						<p>Filing of Application</p>
						<p>+ Filing of Reply</p>
						<p>+ Attending Hearing</p>
						<p><strong><s>5,700/-</s></strong></p>
						<p><strong>4,500/-</strong></p>
					</td>
				</tr>
				<tr style="background-color:#222831;">
					<td colspan="3" valign="top" >
						<div>Application fee (to deposit with trademark office)
						<br>Rs.4,500/- for Individual/Proprietorship Firm
						<br>Rs.9,000/- for Partnership Firm/Company</div>
					</td>
				</tr>
				<tr>
					<td colspan="4" valign="top" style="text-align:center; background-color: #fd7014; "><p><strong>FREE - Search report + Consultation for application</strong></p></td>
				</tr>
				<tr style="background-color:#222831;">
					<td colspan="4" valign="top" >
						<h3 style="text-align:center">TRADEMARK RENEWAL</h3>
						<p><strong>Our Charges Rs.1,000/-,</strong></p>
						<p><strong>Govt. Fee for Renewal Rs.9,000/-,</strong></p>
						<p>
							<strong>Requirements – </strong>
							<br>1. Trademark Application No.
							<br>2. Expenses.
						</p>
						<p><strong>RENEWAL PROCESS WILL BE COMPLETED BY SAME DAY</strong></p>
						<p><strong>PAYMENT RECEIPT &amp; FILING DETAILS WILL BE SHARED IMMEDIATELY</strong></p>
						<p>We are associated with hundreds of CA, CS, law firms, advocates across the nation</p>
					</td>
				</tr>
				<tr>
				<td colspan="4" style="text-align:center; background-color: #fd7014; "><p><strong>slslegal99@gmail.com &emsp;
					www.slslegal.com&emsp;
					Ph.9891665001</strong></p></td>
				</tr>
			</tbody>
		</table>
		<p style="text-align:center"><strong>“आपकी कोई भी कानूनी जरुरत हो - हमसे पूछिये”</strong></p>
	</body>
</html>
'''

msg.add_alternative(htmlContent, subtype='html')

# files=["Shrestha Legal Law Firm profile.pdf"]
# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name
    
#     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
  
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    for n in range(3):
        currentEmail = currentEmailList[n]
        print("Sending Mail To:", currentEmail)
        smtp.send_message(msg)
print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~