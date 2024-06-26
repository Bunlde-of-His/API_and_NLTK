from flask import request, jsonify
import nltk


class NltkApi:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):
        @self.app.route('/tokenize', methods=['POST'])
        def tokenize():
            data = request.get_json()
            text = data.get('text', '')
            tokens = nltk.word_tokenize(text)
            return jsonify(tokens)

        @self.app.route('/pos_tag', methods=['POST'])
        def pos_tag():
            data = request.get_json()
            text = data.get('text', '')
            tokens = nltk.word_tokenize(text)
            pos_tags = nltk.pos_tag(tokens)
            return jsonify(pos_tags)

        @self.app.route('/ner', methods=['POST'])
        def ner():
            data = request.get_json()
            text = data.get('text', '')
            tokens = nltk.word_tokenize(text)
            pos_tags = nltk.pos_tag(tokens)
            named_entities = nltk.ne_chunk(pos_tags)
            entities = []

            current_chunk = []
            for chunk in named_entities:
                if hasattr(chunk, 'label'):
                    current_chunk.append(chunk)
                else:
                    if current_chunk:
                        entity_name = ' '.join([token for subtree in current_chunk for token, pos in subtree.leaves()])
                        entity_type = current_chunk[0].label()
                        entities.append((entity_name, entity_type))
                        current_chunk = []
                    token, pos = chunk
                    if pos in ('NNP', 'NNPS'):
                        entities.append((token, pos))

            if current_chunk:
                entity_name = ' '.join([token for subtree in current_chunk for token, pos in subtree.leaves()])
                entity_type = current_chunk[0].label()
                entities.append((entity_name, entity_type))

            filtered_entities = [(entity, entity_type) for entity, entity_type in entities if
                                 entity_type in ["PERSON", "ORGANIZATION", "GPE", "LOCATION"]]

            return jsonify(filtered_entities)
