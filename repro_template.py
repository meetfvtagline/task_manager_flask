from flask import Flask, render_template
from unittest.mock import MagicMock

app = Flask(__name__, template_folder='app/templates')
app.secret_key = 'test'

@app.route('/')
def index():
    # Mocking tasks
    tasks = [
        MagicMock(id=1, title="Task 1", description="Desc 1", status="pending"),
        MagicMock(id=2, title="Task 2", description="Desc 2", status="in-progress"),
        MagicMock(id=3, title="Task 3", description="Desc 3", status="completed"),
    ]
    
    counts = {
        "pending": 1,
        "in_progress": 1,
        "completed": 1,
    }
    
    # Mock session
    session = {"username": "testuser"}
    
    try:
        return render_template("tasks/dashboard.html", tasks=tasks, counts=counts, session=session)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    with app.test_request_context():
        # Mocking session access in template if needed (it is in base.html)
        # But we need to make sure get_flashed_messages works
        from flask import session
        session['username'] = 'testuser'
        try:
            print(render_template("tasks/dashboard.html", tasks=tasks, counts=counts))
        except Exception as e:
            print(f"FAILED: {e}")
            import traceback
            traceback.print_exc()

# Need to rerun specifically with correct context setup if this fails generally
