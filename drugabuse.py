import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="What You Need to Know About Addiction", page_icon="💊", layout='wide', initial_sidebar_state='expanded')

st.sidebar.write("***Note: This website includes Canadian resources, but the information is suitable for anybody***")
st.sidebar.markdown("<h2 style='color:#FF0000'>Navigate:</h2>", unsafe_allow_html=True)

sect = st.sidebar.radio("", ["Home", "Types of Addiction", "Signs of Addiction", "Available Help Resources", "Sources"])

if sect == "Home":
	
	st.markdown(f"<h1 style='color:#FF0000'>What You Need to Know About Addiction</h1>", unsafe_allow_html=True)
	st.markdown(f"<h3 style='color:#0099AA'>\"Achievement through abstinence\"</h4>", unsafe_allow_html=True)

	st.write("---")	
	st.image("https://leafly-cms-production.imgix.net/wp-content/uploads/2018/05/25115303/estonian-flag-the-roll-up.jpg", caption="https://www.leafly.com/learn/cannabis-glossary/leaf")
	st.write("---")

	st.write("You're coming home from Leaf Life after snagging the biggest cannabis deal you've seen since 2012. You've decided that, once you get home, you're gonna get so high you'll feel like you've been hit by a tranquilizer dart, but instead of going unconscious, you'll feel better than you've ever felt in **years**.")
	st.write("Your friends have been trying to talk you out of it, but you don't care. They don't know how it feels. You drive home in anticipation of the highest hour you've ever had. Once you get home, you open up your pack of cannabis and snort twice the amount you did last week.")
	st.write("However, you don't feel that high. Instead, you feel a bit dizzy for a moment, and then it just stops. You feel good, but not nearly as good as you thought you would. After a few minutes, your mind wanders back to your disapointing life, ruining the moment you thought would last much longer...")
	st.write("---")
	st.write("This is a prime case of addiction. Addiction is a constant reliance on a substance or product to maintain a normal state of mind. You'll feel the need to keep going back to that drug, game or activity that makes you feel good so that you'll feel like a normal person.")
	st.write("Abstinence is the act of staying away from this addictive activity or product. This can mean quitting smoking for a week, locking your drinks away for a month, or deleting your video games to stop you from playing them. All of these are forms of abstinence - keeping yourself away from whatever you're addicted from. While this does help you get out of the addiction, it will require great amounts of willpower and support, since you won't feel very good after you stop doing what you're addicted to.")
	st.write("This happens because of something called ***dopamine***. It's a hormone that makes people feel happy, and is released whenever you do or feel something pleasurable. However, in terms of addiction, when someone repeatedly uses a substance or does an activity, they will feel less and less pleasure over repetitions due to the brain \'getting used to\' the activity or substance. This causes it to lower the amount of dopamine that is released for every use, while also lowering its overall dopamine levels to compensate for the repeated action or usage.")
	st.write("This is what leads to addiction; when you need to continue using a substance or repeat an activity in order to feel ***normal***. Here, I'll discuss the symptoms of addiction, and some substances that can be addictive.")

if sect == "Types of Addiction":
	
	st.markdown(f"<h1 style='color:#FF0000'>{sect}</h1>", unsafe_allow_html=True)

	st.write("---")
	st.image("https://www.farcanada.org/app/uploads/2017/03/brain.gif", caption="https://www.farcanada.org/understanding-addiction/how-do-drugs-affect-the-brain/")
	st.write("There are a few different types of substances that can cause addiction, and they all act in different ways. Here, I'll discuss these different types of substance addictions, and what they might look like.")
	st.write("---")

	addesc = {
		
		"Alcohol": [
			["https://static01.nyt.com/images/2023/01/13/well/13Well-Alcohol/13Well-Alcohol-superJumbo.jpg", "https://www.nytimes.com/2023/01/13/well/mind/alcohol-health-effects.html"],
			"Alcohol is a well-known and common source of addiction. Alcohol is a substance that is normally used for cleaning, but is also used in drinks to give consumers a good feeling - known as ***\'getting high\'***.",
			"In this state, a person's mind enters a *euphoric* state, where risk assesment is impaired and emotional pain is either reduced or emphasized. This leads to those in depression feeling more depressed as they drink, and those who are in a positive state of mind to feel better than normal.",
			"These effects only happen when someone gets *drunk*, which is when they have a concentration of alcohol in their bloodstream that impairs their mental processes. However, this euphoric state has negative effects on a person's brain. If someone drinks too often, they can find themselves to be dependent on the alcohol in order to feel \'normal\'. This is ***alcohol addiction***.",
			"As a person develops a dependence on alcohol, they will need to drink more and more in higher concentrations to feel the same that they did before they started drinking. If they don't, they constantly feel depressed and irritable, while craving more and more for alcohol."
		],
		 
		"Tobacco": [
			["https://cdn.britannica.com/95/138795-050-4F265384/Tobacco.jpg", "https://www.britannica.com/plant/common-tobacco"],
			"Tobacco is a leafy plant that contains high amounts of ***nicotine***. Nicotine is a very addictive substance that triggers dopamine spikes in the brain, making many drugs very addictive. People under the age of 18 tend to be the most suseptible to this addictive substance, which can start affecting them at a young age, and continue to do so over the course of their lives. Tobacco is usually inhaled (\'snorted\') or smoked, though other methods of ingestion may exist."
		],
		
		"Opioids": [
			["https://sa1s3optim.patientpop.com/assets/images/provider/photos/2167715.jpg", "https://www.valleymedical.com/blog/opioids-for-pain-relief-weighing-the-risks-and-benefits"],
			"Opioids are some of the most often abused substances, legal and illegal alike. They are a type of depressants and pain relievers, and get abused in either banned forms like heroin, or in their legal form as pharmaceutical opiates. They include codeine, morphine, oxycodone and hydrocodone.",
			"The dependence on these opioids can easily become very strong, and overuse/abuse can cause severe respiratory issues, and even ***death***."
		],
		"Stimulants": [
			["https://img.gamewith.net/img/fb2b6cfabf31403b93d14c15c552d103.jpg", "https://gamewith.net/cod-modernwarfare/article/show/12269"],
			"No, not that kind of stimulant. Stimulants are drugs that are often abused by people looking for more energy, productivity or alertness. This group includes amphetamines and cocaine. They can also be misused dietary prescriptions. Stimulant abuse often leads to hyperthermia, unprovoked/increased hostility, mood swings, seizures, psychosis and even ***heart failure***."
		],
		
		"Hallucinogens": [
			["https://mydr.com.au/wp-content/uploads/2019/04/hallucinogens.jpg", "https://mydr.com.au/addictions/hallucinogens-what-are-the-effects/"],
			"These drugs distort a person's senses and change the way they percieve reality (in a bad way). Hallucinogens include illegal drugs like MDMA, PCP, LSD and DMT, along with certain mushrooms (like \'magic\' mushrooms), cacti and trees in the wild.",
			"Side effects of hallucinogens and designer drug side effects include dissociative episodes (feeling \'disconnected\' from yourself and/or the world and unpredictability, as well as - during abstinence - ***depression***."
		],
		
		"Cannabis": [
			["https://leafly-cms-production.imgix.net/wp-content/uploads/2018/05/25115303/estonian-flag-the-roll-up.jpg", "https://www.leafly.com/learn/cannabis-glossary/leaf"],
			"This drug is found in many legal medicinal and recreational markets. Cannabis is becoming a drug as accepted as alcohol and tobacco. Abuse of this drug can lead to loss of motiviation and changes (often negative) in perception and cognition (brain activity)."
		]

	}
	adtype = st.selectbox("Substance Type:", addesc.keys())

	st.write("---")
	st.markdown(f"<h2 style='color:cyan'>{adtype}</h2>", unsafe_allow_html=True)

	st.image(addesc[adtype][0][0], caption=addesc[adtype][0][1], width=1000)

	for i in addesc[adtype][1:]:
		st.write(i)

if sect == "Signs of Addiction":

	st.markdown(f"<h1 style='color:#FF0000'>{sect}</h1>", unsafe_allow_html=True)


	st.write("---")
	st.image("https://www.verywellmind.com/thmb/oT7rs4hn4VZAmfxc7WJB_9hlkik=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-185327528web-570bcbf93df78c7d9ef69eb6.jpg", caption="https://www.verywellmind.com/understanding-an-addict-21927")
	st.write("---")

	st.subheader("Some signs of addiction:")

	signs = [
		"**Sudden changes in behaviour or personality** - can include the presence of (or increase in) irritability, mood swings, agitation, anxiety or self-doubt.",
		"**Bloodshot eyes/bloody nose** - likely signs of drug overconsumption.",
		"**Lack of physical control** - tremors, shaking, muscle spasms or other uncontrollable activity.",
		"**Slurred speech** - either due to recent usage or an overload in usage.",
		"**Changes in regular routines** - where someone changes something that they've done regularly over a long period of time.",
		"**Lower standards of hygiene** - if someone does not keep themselves as \'clean\' as they've normally done.",
		"**Suddenly having new or different friends/not maintaining relationships with other friends** - this could indicate that a person has joined a group of drug abusers or something similar.",
		"**Losing a job or needing more money** - may be a change in priorities from needs to drugs, as well as spending more on drugs, leaving little money for other things."
	]

	for i in signs:
		st.write(f" - {i}")


if sect == "Available Help Resources":

	st.markdown(f"<h1 style='color:#FF0000'>{sect}</h1>", unsafe_allow_html=True)
	st.write("---")
	st.image("https://cdn.britannica.com/68/7068-004-7848FEB4/Flag-Canada.jpg", caption="https://www.britannica.com/topic/flag-of-Canada")
	st.write("---")

	c1, c2 = st.columns(2)

	with c1:

		with st.expander("Wellness Together Canada"):

			st.markdown(f"<h2 style='color:#FF0000'>Wellness Together Canada</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://ca.portal.gs/</h5>", unsafe_allow_html=True)
			st.write(" - Immediate, free and confidential mental health and substance use help\n - 24/7\n - Virtual services in English and French\n - Interpretation services available during phone-counselling sessions in over 200 languages and dialects")

		with st.expander("Kids Help Phone"):

			st.markdown(f"<h2 style='color:#FF0000'>Kids Help Phone</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://kidshelpphone.ca/</h5>", unsafe_allow_html=True)
			st.write(" - Professional counselling, information and referrals support to young people\n - 24/7\n - Virtual services in English and French")

		with st.expander("Drug Rehab Services"):

			st.markdown(f"<h2 style='color:#FF0000'>Drug Rehab Services</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://www.drugrehab.ca/</h5>", unsafe_allow_html=True)
			st.write(" - Free, confidential professional help and resource for drug and alcohol addiction in Canada\n - Referrals for clients seeking support with substances")

		with st.expander("SMART Recovery"):

			st.markdown(f"<h2 style='color:#FF0000'>SMART Recovery</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://www.smartrecovery.org/</h5>", unsafe_allow_html=True)
			st.write(" - Free support meetings (in-person and virtual) open to anyone seeking science-based, self-empowered addiction recovery")

	with c2:

		with st.expander("CAPSA Peer Support"):

			st.markdown(f"<h2 style='color:#FF0000'>CAPSA Peer Support</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://capsa.ca/peer-support/</h5>", unsafe_allow_html=True)
			st.write(" - Free peer-facilitated group meetings (includes virtual meetings)\n - Evidence-based practices and tools designed to help those who are questioning their relationship with substances\n - Families, allies, and professionals are all welcome to attend meetings")

		with st.expander("Alcoholics Anonymous"):

			st.markdown(f"<h2 style='color:#FF0000'>Alcoholics Anonymous</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://www.aa.org/</h5>", unsafe_allow_html=True)
			st.write(" - Free meetings and support for people who come together to solve their drinking problem")

		with st.expander("Narcotics Anonymous"):

			st.markdown(f"<h2 style='color:#FF0000'>Narcotics Anonymous</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://canaacna.org/</h5>", unsafe_allow_html=True)
			st.write(" - Free meetings (includes virtual) and support for anyone who wants to stop using drugs may become a member\n - This is a program of complete abstinence from all drugs")

		with st.expander("Families for Addiction Recovery"):

			st.markdown(f"<h2 style='color:#FF0000'>Families for Addiction Recovery</h2>", unsafe_allow_html=True)	
			st.markdown(f"<h5 style='color:#0099FF'>Website: https://www.farcanada.org/</h5>", unsafe_allow_html=True)
			st.write(" - Free peer support services for families, parents, caregivers of children struggling with addiction (regardless of age)")

	st.markdown(f"<h5 style='color:#FFFF00'>Learn more at: https://www.canada.ca/en/health-canada/services/substance-use/get-help-with-substance-use.html</h5>", unsafe_allow_html=True)

if sect == "Sources":

	src = {
		"Different Types and Causes of Substance Abuse - San Diego | API": "https://apibhs.com/2017/12/11/types-causes-of-substance-abuse",
		"Types of Substance Abuse: Different Types of Addiction | Infinite Recovery": "https://www.infiniterecovery.com/substance-abuse/types-of-substance-abuse/",
		"Get Help With Substance Use - Canada.ca": "https://www.canada.ca/en/health-canada/services/substance-use/get-help-with-substance-use.html"
	}

	for i in src:
		st.write(f"- [{i}]({src[i]})")
