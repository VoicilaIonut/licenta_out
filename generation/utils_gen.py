import os
from datetime import datetime


def to_csv(df, filename):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(filename)
    filename = f"{base}_{current_time}{ext}"

    df.to_csv(filename, index=False)
    print(f"DataFrame successfully saved to {filename}")


class Rephraser:
    def gen(self, text, text_to_rephrase):
        return len(text_to_rephrase) * "#"  # Dummy rephraser

    def compute_query(self, text, query):
        if query == "rephrase":
            return "Rescrie următorul text:\n" + text
        elif query == "summarize":
            return "Rezumă următorul text:\n" + text
        elif query == "continue":
            half_text = text.split("\n")
            half_text = "\n".join(half_text[: len(half_text) // 2])

            return "Continuă următorul text:\n" + half_text
        elif query == "non_ai_doctorat":
            return "Reformulează textul următor, extras dintr-un subcapitol de teză doctorală, astfel încât să pară scris de un doctorand român și să nu poată fi identificat ca fiind generat de inteligență artificială:\n" + text
        elif query == "non_ai_doctorat_summary":
            return "Rescrie textul următor, extras dintr-un subcapitol de teză doctorală, într-o formă prescurtată, astfel încât să pară scris de un doctorand român și să nu poată fi identificat ca fiind generat de inteligență artificială:\n" + text
        elif query == "non_ai_doctorat_continue":
            half_text = text.split("\n")
            half_text = "\n".join(half_text[: len(half_text) // 2])
            return "Continuă textul următor, extras dintr-un subcapitol de teză doctorală, astfel încât să pară scris de un doctorand român și să nu poată fi identificat ca fiind generat de inteligență artificială:\n" + half_text
        elif query == "expert":
            return "Rescrie următorul text ca un expert în domeniu:\n" + text
        elif query == "intelesul_tuturor":
            return "Rescrie următorul text ca sa fie pe înțelesul tuturor:\n" + text
        elif query == "non_ai":
            return "Rescrie următorul text ca să fie asemanator omului și nedetectabil de un detector de text generat:\n" + text
        elif query =="doctorat_specific":
            return "Rescrie următorul paragraf dintr-un subcapitol dintr-o lucrare de doctorat ca și cum ai fi un doctorand român. Textul ar trebui să reflecte stilul, tonul, nivelul de formalitate și posibilele particularități ale acestei persoane.\n" + text
        elif query == "doctorat":
            return "Rescrie următorul text dintr-un subcapitol al unei lucrări de doctorat precum un doctorand român:\n" + text
            
        else:
            raise ValueError("Unknown query type")


# def compute_costum_query(text_to_rephrase, query_task):
#     if query_task == "expert":
#         return "Rescrie următorul text ca un expert în domeniu:\n" + text_to_rephrase
#     elif query_task == "intelesul_tuturor":
#         return "Rescrie următorul text ca sa fie pe înțelesul tuturor:\n" + text_to_rephrase
#     elif query_task == "non_ai":
#         return "Rescrie următorul text ca să fie asemanator omului și nedetectabil de un detector de text generat:\n" + text_to_rephrase
#     elif query_task =="doctorat_specific":
#         return "Rescrie următorul paragraf dintr-un subcapitol dintr-o lucrare de doctorat ca și cum ai fi un doctorand român. Textul ar trebui să reflecte stilul, tonul, nivelul de formalitate și posibilele particularități ale acestei persoane.\n" + text_to_rephrase
#     elif query_task == "doctorat":
#         return "Rescrie următorul text dintr-un subcapitol al unei lucrări de doctorat precum un doctorand român:\n" + text_to_rephrase
#     elif query_task == "non_ai_doctorat":
#         return "Reformulează textul următor, extras dintr-un subcapitol de teză doctorală, astfel încât să pară scris de un doctorand român și să nu poată fi identificat ca fiind generat de inteligență artificială:\n" + text_to_rephrase
#     elif query_task == "non_ai_doctorat_summary":
#         return "Rescrie textul următor, extras dintr-un subcapitol de teză doctorală, într-o formă prescurtată, astfel încât să pară scris de un doctorand român și să nu poată fi identificat ca fiind generat de inteligență artificială:\n" + text_to_rephrase
#     elif query_task == "non_ai_doctorat_continue":
#         half_text = text_to_rephrase.split("\n")
#         half_text = "\n".join(half_text[: len(half_text) // 2])
#         return "Continuă textul următor, extras dintr-un subcapitol de teză doctorală, astfel încât să pară scris de un doctorand român și să nu poată fi identificat ca fiind generat de inteligență artificială:\n" + half_text
#     else:
#         raise ValueError("Unknown query task")