def calculates_results_stats(results_dic):
        
    results_stats_dic = dict()
    
    results_stats_dic['n_images'] = 0 #
    results_stats_dic['n_dogs_img'] = 0 #
    results_stats_dic['n_notdogs_img'] = 0 #
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0 #
    results_stats_dic['n_correct_notdogs'] = 0 #
    results_stats_dic['n_correct_breed'] = 0  #
    
    
    for key in results_dic:
       
        results_stats_dic['n_images'] = len(results_dic)
        
        
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
        
        if results_dic[key][3] == 1: 
            
            
            results_stats_dic['n_dogs_img'] += 1
            
            if results_dic[key][4] == 1: # Classifier Lable is Dog
                # Number of Correct Dog matches
                results_stats_dic['n_correct_dogs'] += 1
            
            if results_dic[key][2] == 1: 
                results_stats_dic['n_correct_breed'] += 1
        
        else: 
            results_stats_dic['n_notdogs_img'] += 1
            
            if results_dic[key][4] == 0: # Classifier Lable is NOT Dog
                # Number of Correct Non-Dog matches
                results_stats_dic['n_correct_notdogs'] += 1
                
                
        results_stats_dic['pct_match'] = results_stats_dic['n_match'] / results_stats_dic['n_images'] * 100
           
        if results_stats_dic['n_dogs_img'] > 0:
            # pct_correct_dogs - percentage of correctly classified dogs
            results_stats_dic['pct_correct_dogs'] = results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img'] * 100
            # pct_correct_breed - percentage of correctly classified dog breeds
            results_stats_dic['pct_correct_breed'] = results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img'] * 100
        else:
            results_stats_dic['pct_correct_dogs'] = 0
            results_stats_dic['pct_correct_breed'] = 0
    
        # pct_correct_notdogs - percentage of correctly classified NON-dogs
        if results_stats_dic['n_notdogs_img'] > 0:
            results_stats_dic['pct_correct_notdogs'] = results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img'] * 100
        else:
            results_stats_dic['pct_correct_notdogs'] = 0
            
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    return results_stats_dic
