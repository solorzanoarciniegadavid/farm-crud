from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return 'Holi poli holi'

@app.get('/home')
def welcome():
    return 'Home'

@app.get('/api/tasks')
async def get_tasks():
    return 'all tasks'

@app.post('/api/tasks')
async def create_task():
    return 'create task'

@app.get('/api/tasks/{id}')
async def get_task():
    return 'single task'

@app.put('/api/tasks/{id}')
async def update_task():
    return 'all tasks'

@app.delete('/api/tasks/{id}')
async def delete_task():
    return 'all tasks'