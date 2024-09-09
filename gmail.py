import smtplib
import ssl
from email.message import EmailMessage
from Speak2 import Speak
def gmail():
    while True:
        
        email_receiver = input("Enter the Gmail:")
        if "exit" in email_receiver:
            break
        else:

            email_sender = "cutomers85@gmail.com"
            email_password = "lnpatxhxlecbykxi"

            subject = "SUSTAINABLE DEVELOPMENT GOALS"
            body = '''I hope this email finds you well. Today, I wanted to take a moment to discuss an important global initiative that aims to create a better and more sustainable future for all of us - the Sustainable Development Goals (SDGs).

            The SDGs were adopted by all United Nations Member States in 2015 as a universal call to action to end poverty, protect the planet, and ensure prosperity for everyone by the year 2030. These 17 goals form a comprehensive and interconnected framework that addresses various social, economic, and environmental challenges facing our world today.

            Here is a brief overview of the SDGs:

            1. No Poverty: End poverty in all its forms everywhere.
            2. Zero Hunger: End hunger, achieve food security and improved nutrition, and promote sustainable agriculture.
            3. Good Health and Well-being: Ensure healthy lives and promote well-being for all at all ages.
            4. Quality Education: Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.
            5. Gender Equality: Achieve gender equality and empower all women and girls.
            6. Clean Water and Sanitation: Ensure availability and sustainable management of water and sanitation for all.
            7. Affordable and Clean Energy: Ensure access to affordable, reliable, sustainable, and modern energy for all.
            8. Decent Work and Economic Growth: Promote sustained, inclusive, and sustainable economic growth, full and productive employment, and decent work for all.
            9. Industry, Innovation, and Infrastructure: Build resilient infrastructure, promote inclusive and sustainable industrialization, and foster innovation.
            10. Reduced Inequality: Reduce inequality within and among countries.
            11. Sustainable Cities and Communities: Make cities and human settlements inclusive, safe, resilient, and sustainable.
            12. Responsible Consumption and Production: Ensure sustainable consumption and production patterns.
            13. Climate Action: Take urgent action to combat climate change and its impacts.
            14. Life Below Water: Conserve and sustainably use the oceans, seas, and marine resources for sustainable development.
            15. Life on Land: Protect, restore, and promote sustainable use of terrestrial ecosystems, manage forests sustainably, combat desertification, halt and reverse land degradation, and halt biodiversity loss.
            16. Peace, Justice, and Strong Institutions: Promote peaceful and inclusive societies for sustainable development, provide access to justice for all, and build effective, accountable, and inclusive institutions at all levels.
            17. Partnerships for the Goals: Strengthen the means of implementation and revitalize the global partnership for sustainable development.

            These goals, though ambitious, offer a roadmap for collective action and represent a commitment by countries and organizations worldwide to work together towards a more just, equitable, and sustainable world.

            To learn more about the SDGs and how you can get involved, please visit the following link: https://sdgs.un.org/goals

            Let us join hands and contribute our part in achieving these global goals for a brighter future for humanity and the planet.

            Thank you for your attention, and if you have any questions or thoughts, feel free to reach out.'''

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
                
            print("Sent")
gmail()

            