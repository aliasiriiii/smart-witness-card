
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from weasyprint import HTML
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/generate_card', methods=['POST'])
def generate_card():
    @app.route('/analyze_text', methods=['POST'])
def analyze_text():
    input_text = request.json.get("input_text", "")
    
    if not input_text:
        return {"error": "No input_text provided"}, 400

    # استجابة وهمية كمثال (تقدر تربط GPT لاحقًا)
    result = {
        "analysis": f"تم تحليل الشاهد: {input_text[:50]}... ✅"
    }
    return result
    program_name = request.form.get('program_name', '---')
    instructor = request.form.get('instructor', '---')
    category = request.form.get('category', '---')
    job_description = request.form.get('job_description', '---')
    objectives = request.form.get('objectives', '---')
    description = request.form.get('description', '---')
    date = request.form.get('date', '---')
    duration = request.form.get('duration', '---')
    beneficiaries = request.form.get('beneficiaries', '---')
    teacher_signature = request.form.get('teacher_signature', '---')
    manager_signature = request.form.get('manager_signature', '---')

    image1 = request.files.get('image1')
    image2 = request.files.get('image2')

    image1_path = os.path.join(UPLOAD_FOLDER, secure_filename(image1.filename))
    image2_path = os.path.join(UPLOAD_FOLDER, secure_filename(image2.filename))
    image1.save(image1_path)
    image2.save(image2_path)

    html_content = f'''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: 'Arial', sans-serif;
                direction: rtl;
                padding: 20px;
                border: 2px solid #444;
                margin: 20px;
            }
            h2 {
                text-align: center;
                color: #2c3e50;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            td {
                padding: 8px;
                border: 1px solid #aaa;
                vertical-align: top;
            }
            .label {
                background-color: #f0f0f0;
                font-weight: bold;
                width: 25%;
            }
            .signature {
                margin-top: 30px;
                text-align: center;
            }
            .images {
                margin-top: 30px;
                text-align: center;
            }
            .images img {
                width: 45%;
                margin: 10px;
                border: 1px solid #ccc;
            }
        </style>
    </head>
    <body>
        <h2>بطاقة توثيق شاهد ذكي</h2>
        <table>
            <tr><td class="label">اسم البرنامج:</td><td>{program_name}</td></tr>
            <tr><td class="label">منفذ البرنامج:</td><td>{instructor}</td></tr>
            <tr><td class="label">مجال البرنامج:</td><td>{category}</td></tr>
            <tr><td class="label">الوصف الوظيفي:</td><td>{job_description}</td></tr>
            <tr><td class="label">أهداف البرنامج:</td><td>{objectives}</td></tr>
            <tr><td class="label">وصف التنفيذ:</td><td>{description}</td></tr>
            <tr><td class="label">تاريخ التنفيذ:</td><td>{date}</td></tr>
            <tr><td class="label">مدة التنفيذ:</td><td>{duration}</td></tr>
            <tr><td class="label">عدد المستفيدين:</td><td>{beneficiaries}</td></tr>
        </table>

        <div class="images">
            <h3>صور مرفقة توثق الشاهد:</h3>
            <img src="file://{image1_path}" alt="صورة 1"/>
            <img src="file://{image2_path}" alt="صورة 2"/>
        </div>

        <div class="signature">
            <p>توقيع المعلم: {teacher_signature}</p>
            <p>توقيع مدير المدرسة: {manager_signature}</p>
        </div>
    </body>
    </html>
    '''

    output_pdf_path = os.path.join(UPLOAD_FOLDER, "smart_witness_card.pdf")
    HTML(string=html_content).write_pdf(output_pdf_path)
    return send_file(output_pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
