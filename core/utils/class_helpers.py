class ModelFullName:
    def get_full_name(self, modelInstance):
        if self.Meta.model.__name__ == 'Province':
            return f'Tỉnh {modelInstance.name}' if modelInstance.type == 'P' else f'Thành Phố {modelInstance.name}'
        elif self.Meta.model.__name__ == 'District':
            if modelInstance.type == 'C':
                return f'Thành Phố {modelInstance.name}'
            elif modelInstance.type == 'UD':
                return f'Quận {modelInstance.name}'
            elif modelInstance.type == 'RD':
                return f'Huyện {modelInstance.name}'
            else:
                return f'Thị Xã {modelInstance.name}'
        else:
            if modelInstance.type == 'C':
                return f'Xã {modelInstance.name}'
            elif modelInstance.type == 'W':
                return f'Phường {modelInstance.name}'
            else:
                return f'Thị Trấn {modelInstance.name}'
