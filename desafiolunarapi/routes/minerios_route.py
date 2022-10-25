import desafiolunarapi.repository as rep

def routes(app, template, request):

    @app.route('/')
    def index():
        return template('index.html')

    @app.route("/minerios",  methods=['GET'])
    def all(): return rep.all()

    @app.route("/minerios/<int:id>",  methods=['GET'])
    def find(id):
        return rep.find_by_id(id) 

    @app.route("/minerios",  methods=['POST'])
    def create(): rep.create(request.json)

    @app.route("/minerios/<int:id>",  methods=['PUT'])
    def edit(id): rep.edit(id, request.json)

    @app.route("/minerios/<int:id>",  methods=['DELETE'])
    def remove(id): rep.remove(id)
