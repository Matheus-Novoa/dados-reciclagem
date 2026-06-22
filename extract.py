import zipfile
from pathlib import Path

def extrair_e_deletar_zips(caminho_pasta: str):
    # Converte para caminho absoluto baseado de onde o script está sendo executado
    pasta_alvo = Path(caminho_pasta).resolve()
    
    if not pasta_alvo.exists():
        print(f"❌ Diretório não encontrado: {pasta_alvo}")
        return
        
    # Procura todos os arquivos .zip na pasta
    arquivos_zip = list(pasta_alvo.glob("*.zip"))
    
    if not arquivos_zip:
        print(f"⚠️ Nenhum arquivo .zip encontrado em: {pasta_alvo}")
        return
        
    print(f"📦 Encontrados {len(arquivos_zip)} arquivo(s) compactado(s).\n")
    
    for zip_path in arquivos_zip:
        print(f"⏳ Extraindo: {zip_path.name} ...")
        try:
            # Abre e extrai o arquivo
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(pasta_alvo)
            print(f"✅ {zip_path.name} extraído com sucesso!")
            
            # Deleta o arquivo .zip apenas se a extração correu bem
            zip_path.unlink()
            print(f"🗑️  Arquivo compactado deletado para liberar espaço.")
            print("-" * 40)
            
        except Exception as e:
            print(f"❌ Erro ao processar {zip_path.name}: {e}")
            print("-" * 40)
            
    print("\n🚀 Processo concluído! Espaço em disco recuperado.")

if __name__ == "__main__":
    # Mantendo o caminho relativo padrão do projeto
    CAMINHO_DADOS = "data/raw"
    extrair_e_deletar_zips(CAMINHO_DADOS)