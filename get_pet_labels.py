
from os import listdir


def get_pet_labels(image_dir):
    
    filename_list = listdir(image_dir)
    
    print('\n10 filenames from folder pet_images')
    
    # create empty list for pet labels
    pet_labels = []
    
    # create empty dictionary    
    results_dic = dict()
    
    # iterate over each file name to save the pet name individually
    for index in range(0, len(filename_list), 1):
        if filename_list[index][0] != ".":
            pet_label = ''
            pet_image_filename = filename_list[index]
            word_list_pet_image_filename = pet_image_filename.lower().split('_')
            pet_name = ''
            
            for word in word_list_pet_image_filename:
                if word.isalpha():
                    pet_name += word + " "
            
            pet_name = pet_name.strip()
            print('Filename = ', pet_image_filename, '    label = ', pet_name)
           
                      
            print('\n{:2d} file: {:>25}'.format(index + 1, filename_list[index]))
   
            # count length of empty dictionary
            number_of_items_empty_dic = len(results_dic)
    
            print('\nEmpty dictionary has {} items'.format(number_of_items_empty_dic))
    
            # add every element of pet_labels as a value to the results_dic
            if filename_list[index] not in results_dic:
                results_dic[filename_list[index]] = [pet_name]# what does filenames refer to, here?
            else:
                print('\nWARNING: key =' , filenames[index],  'already exists in results_dic with value =', results_dic[filenames[index]])
          
    print('\nPrinting all key-value pairs in dictionary results_dic:')
    for key in results_dic:
          print('\nfilename = ', key, '    pet label = ', results_dic[key][0])
            
    # count length in full dictionary
    number_of_items_full_dic = len(results_dic)
    print('\nEmpty dictionary has {} items'.format(number_of_items_full_dic))
    
          
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
