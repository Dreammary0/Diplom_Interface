from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)


@app.route('/get_graphs_parameters', methods=['POST'])
def get_graphs_parameters():
    parameters_for_graph = request.get_json()
    # здесь можно выполнить какие-то действия с полученными данными

    return jsonify("/static/img/graph.png")


@app.route('/get_DBSCAN_parameters', methods=['POST'])
def get_DBSCAN_parameters():
    parameters_for_DBSCAN = request.get_json()
    # здесь можно выполнить какие-то действия с полученными данными
    time.sleep(5)
    return jsonify(parameters_for_DBSCAN)


@app.route('/')
def index():
    clustering_params = {'weight_distance': 2, 'weight_speed': 1, 'weight_course': 20, 'eps': 0.29, 'min_samples': 50}
    graph_params = {'distance_delta': 50, 'angle_of_vision': 15, 'weight_time_graph': 1, 'weight_course_graph': 3}

    return render_template('index.html',
                           clustering_params=clustering_params,
                           graph_params=graph_params,
                           int=int,
                           len=len
                           )

if __name__ == '__main__':
    app.run(debug=True)
