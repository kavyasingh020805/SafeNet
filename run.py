from app import create_app

app = create_app()

# ✅ Add this route to test your server
@app.route('/')
def home():
    return 'SafeNet Backend is Running ✅'

if __name__ == '__main__':
    app.run(debug=True)
