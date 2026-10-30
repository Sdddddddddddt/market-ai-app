import flet as ft
import google.generativeai as genai

# ضع مفتاح الـ API الخاص بك هنا
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=GEMINI_API_KEY)

def main(page: ft.Page):
    page.title = "Sovereign Market Maker AI"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    result_text = ft.Text("اضغط على الزر أدناه لتشغيل البرومت السيادي وتحليل السوق...", color=ft.colors.WHITE, size=14)

    def analyze_market(e):
        result_text.value = "جاري الاتصال بالمحرك السيادي وتحليل السيولة..."
        page.update()
        
        try:
            model = genai.GenerativeModel(model_name="gemini-2.5-flash")
            sovereign_prompt = """
            [SYSTEM: ULTIMATE INSTITUTIONAL MARKET MAKER & HFT SOVEREIGN CORE v10.0]
            قم بتحليل البيانات واستخراج: المدى الزمني، النسبة الاحتمالية، القرار (صعود 🟢 / هبوط 🔴)، والسبب التكتيكي.
            """
            response = model.generate_content([sovereign_prompt])
            result_text.value = response.text
        except Exception as ex:
            result_text.value = f"خطأ في الاتصال: {str(ex)}"
        
        page.update()

    fab = ft.FloatingActionButton(
        icon=ft.icons.ANALYTICS,
        text="تحليل السيولة",
        bgcolor=ft.colors.AMBER_ACCENT,
        on_click=analyze_market
    )

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("👑 النظام السيادي للخيارات الثنائية", color=ft.colors.AMBER, size=18, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                result_text
            ], alignment=ft.MainAxisAlignment.START),
            padding=20,
            expand=True
        )
    )
    page.floating_action_button = fab

ft.app(target=main)
