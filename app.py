from flask import Flask, request, jsonify
from modules.task import Task

app = Flask(__name__)
print('Running 🔥🔥')

    #CRUD:
    #Create = Criar
    #Read = Ler
    #Update = Atualizar
    #Delete = Deletar

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data['title'],  description=data.get('description', ""))
      # ou pode ser feito dessa forma:
      ## new_task = Task(title=data.get('title'), description=data.get('description', ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({"mensagem": "Nova tarefa criada com sucesso"})
      # ou pode ser feito dessa forma:
      # return 'Nova tarefa crios com sucesso'

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = [ task.to_dict() for task in tasks ]
 
  output = {
            "tasks": task_list,
            "total_tasks": len(tasks)
          }
  return jsonify(output)

if __name__ == "__main__":
  app.run(debug=True)