import desafiolunarapi.infra.repositories.resources_repository as rep

def routes(app, template, request):

    @app.route('/')
    def index():
        return template('index.html')

    @app.route("/resources",  methods=['GET'])
    def all(): return rep.all()

    @app.route("/resources/<int:id>",  methods=['GET'])
    def find(id):
        return rep.find_by_id(id) 

    @app.route("/resources",  methods=['POST'])
    def create(): rep.create(request.json)

    @app.route("/resources/<int:id>",  methods=['PUT'])
    def edit(id): rep.edit(id, request.json)

    @app.route("/resources/<int:id>",  methods=['DELETE'])
    def remove(id): rep.remove(id)