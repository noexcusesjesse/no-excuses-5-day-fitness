from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, KeepTogether
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
red=colors.HexColor("#c91e25")
ink=colors.HexColor("#142033")
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleX",fontName="Helvetica-Bold",fontSize=20,leading=25,textColor=ink,spaceAfter=12))
styles.add(ParagraphStyle(name="DayX",fontName="Helvetica-Bold",fontSize=13,leading=17,textColor=red,spaceBefore=12,spaceAfter=7))
styles.add(ParagraphStyle(name="BodyX",fontName="Helvetica",fontSize=9,leading=13,spaceAfter=5))
story=[Paragraph("NO EXCUSES | FREE 5-DAY FITNESS PROGRAM",styles["TitleX"]),Paragraph("Resistance bands and tubes • Kettlebells • Bodyweight • Walking",styles["BodyX"]),Paragraph("<b>Workout days:</b> Monday, Tuesday, Wednesday, Friday, Saturday. <b>Thursday:</b> active recovery. <b>Sunday:</b> 3 × 20-minute easy walks. <b>Walking goal Monday–Saturday:</b> 10,000 steps OR 90 minutes; begin at your current ability.",styles["BodyX"]),Paragraph("<b>Workout format:</b> 5-minute warm-up + 20-minute circuit + 5-minute cooldown. Two rounds; aim for 10–12 controlled reps, except timed carries. Rest 30–60 seconds or longer if needed.",styles["BodyX"])]
workouts=[
("MONDAY | FULL-BODY STRENGTH",[("Kettlebell goblet squat","Chair squat"),("Resistance tube row","Light or seated band row"),("Wall push-up","Higher wall push-up"),("Kettlebell deadlift","Unweighted hip hinge")]),
("TUESDAY | UPPER BODY + CORE",[("Band chest press","Wall push-up"),("Tube biceps curl","Light band curl"),("Kettlebell suitcase carry, 20–30 sec per side","Unweighted march"),("Standing knee raises","Seated knee raises")]),
("WEDNESDAY | LOWER BODY + BALANCE",[("Kettlebell deadlift","Unweighted hip hinge"),("Band lateral steps","Supported side steps"),("Chair squat","Assisted sit-to-stand"),("Standing calf raise","Supported calf raise")]),
("FRIDAY | FULL-BODY STRENGTH",[("Kettlebell goblet squat","Chair squat"),("Resistance tube row","Seated band row"),("Incline push-up","Wall push-up"),("Kettlebell farmer carry, 20–30 sec","Unweighted march")]),
("SATURDAY | BODYWEIGHT + CONDITIONING",[("Chair sit-to-stands","Assisted sit-to-stand"),("Band pull-aparts","Light band pull-aparts"),("Kettlebell deadlift","Unweighted hip hinge"),("Standing knee raises","Seated knee raises")])]
for title,moves in workouts:
 rows=[[Paragraph("<b>Exercise</b>",styles["BodyX"]),Paragraph("<b>Beginner option</b>",styles["BodyX"])]]
 rows += [[Paragraph(a,styles["BodyX"]),Paragraph(b,styles["BodyX"])] for a,b in moves]
 t=Table(rows,colWidths=[3.4*inch,3.4*inch],hAlign="LEFT")
 t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#ecf0f4")),("LINEBELOW",(0,0),(-1,-1),.4,colors.HexColor("#d6dbe2")),("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),4)]))
 story.append(KeepTogether([Paragraph(title,styles["DayX"]),t]))
story += [Paragraph("THURSDAY | ACTIVE RECOVERY",styles["DayX"]),Paragraph("No strength workout. Easy walking, mobility or gentle stretching as tolerated.",styles["BodyX"]),Paragraph("SUNDAY | WALKING-ONLY RECOVERY",styles["DayX"]),Paragraph("Morning 20 minutes + afternoon 20 minutes + evening 20 minutes. Total 60 minutes at an easy pace.",styles["BodyX"]),Paragraph("WEEKLY PROGRESS TRACKER",styles["DayX"])]
rows=[["Day","Workout","Steps / walking minutes","How I felt"]]+[[d,"__________","________________","____________"] for d in ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")]
t=Table(rows,colWidths=[.8*inch,1.4*inch,2.5*inch,2.1*inch],rowHeights=[24]+[27]*7)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),ink),("TEXTCOLOR",(0,0),(-1,0),colors.white),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("FONTSIZE",(0,0),(-1,-1),8),("GRID",(0,0),(-1,-1),.5,colors.HexColor("#cdd3da"))]))
story += [t,Spacer(1,14),Paragraph("4-WEEK PROGRESSION",styles["DayX"]),Paragraph("Week 1: learn technique. Week 2: add reps if ready. Week 3: consider a third round if time allows. Week 4: increase resistance slightly while maintaining form.",styles["BodyX"]),Paragraph("HEALTH & SAFETY DISCLAIMER",styles["DayX"]),Paragraph("General educational information only, not individualized medical advice. Consult a healthcare professional before starting if you have a medical condition, injury or concern. Check resistance equipment and anchors. Stop if you experience concerning symptoms; seek urgent help for chest pain or severe breathing difficulty. Results vary.",styles["BodyX"]),Spacer(1,12),Paragraph("<b>One Step. No Excuses. Let's Start. One!</b>",styles["BodyX"])]
doc=SimpleDocTemplate("workout-plan.pdf",pagesize=letter,leftMargin=45,rightMargin=45,topMargin=42,bottomMargin=45)
doc.build(story)
print("Generated workout-plan.pdf")
