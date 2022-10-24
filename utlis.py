import pyfreeling
import sys

## -----------------------------------------------
## Do whatever is needed with analyzed sentences
## -----------------------------------------------
def ProcessSentences(ls):
    
    result = []
    for s in ls :
        for w in s :
            result += [f'{w.get_form()}/{w.get_tag()}']

    return result


## -----------------------------------------------
## Set desired options for morphological analyzer
## -----------------------------------------------
def my_maco_options(lang,lpath) :

    # create options holder 
    opt = pyfreeling.maco_options(lang);

    # Provide files for morphological submodules. Note that it is not 
    # necessary to set file for modules that will not be used.
    opt.UserMapFile = "";
    opt.LocutionsFile = lpath + "locucions.dat"; 
    opt.AffixFile = lpath + "afixos.dat";
    opt.ProbabilityFile = lpath + "probabilitats.dat"; 
    opt.DictionaryFile = lpath + "dicc.src";
    opt.NPdataFile = lpath + "np.dat"; 
    opt.PunctuationFile = lpath + "../common/punct.dat"; 
    return opt;



def freeling_analyze(text):
  pyfreeling.util_init_locale("default");

  lang = "es"
  ipath = "/usr/local";
  lpath = ipath + "/share/freeling/" + lang + "/"
  tk=pyfreeling.tokenizer(lpath+"tokenizer.dat");
  sp=pyfreeling.splitter(lpath+"splitter.dat");

  morfo=pyfreeling.maco(my_maco_options(lang,lpath));
  morfo.set_active_options (False,  # UserMap 
                            True,  # NumbersDetection,  
                            True,  # PunctuationDetection,   
                            True,  # DatesDetection,    
                            True,  # DictionarySearch,  
                            True,  # AffixAnalysis,  
                            False, # CompoundAnalysis, 
                            True,  # RetokContractions,
                            True,  # MultiwordsDetection,  
                            True,  # NERecognition,     
                            False, # QuantitiesDetection,  
                            True); # ProbabilityAssignment                 

  tagger = pyfreeling.hmm_tagger(lpath+"tagger.dat",True,2)



  lw = tk.tokenize(text)
  ls = sp.split(lw)

  # perform morphosyntactic analysis and disambiguation
  ls = morfo.analyze(ls)
  ls = tagger.analyze(ls)
  
  return ProcessSentences(ls)