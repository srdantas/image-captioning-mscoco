import os
import keras


class MsCoco:
    
    @staticmethod
    def __download_annotations(name_of_zip='captions.zip'):
        annotation_zip = keras.utils.get_file(
            name_of_zip,
            cache_subdir=os.path.abspath('.'),
            origin='http://images.cocodataset.org/annotations/annotations_trainval2014.zip',
            extract=True)
        return f'{os.path.dirname(annotation_zip)}/annotations/captions_train2014.json'
    
    @staticmethod
    def __download_dataset(name_of_zip='train2014.zip', folder_to_extract='train2014'):
        if not os.path.exists(f'{os.path.abspath(".")}/{name_of_zip}'):
            image_zip = keras.utils.get_file(
                name_of_zip,
                cache_subdir=os.path.abspath('.'),
                origin='http://images.cocodataset.org/zips/train2014.zip',
                extract=True)
            return f'{os.path.dirname(image_zip)}/{folder_to_extract}/'
        else:
            return f'{os.path.abspath(".")}/{folder_to_extract}/'

    def download(self, dataset_name_of_zip='train2014.zip',
                 dataset_folder_to_extract='train2014',
                 annotations_name_of_zip='captions.zip'):
        return self.__download_annotations(annotations_name_of_zip), \
               self.__download_dataset(dataset_name_of_zip, dataset_folder_to_extract)


if __name__ == '__main__':
    MsCoco().download()

