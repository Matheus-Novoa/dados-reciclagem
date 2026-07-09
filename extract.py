import zipfile
from pathlib import Path

def extrair_e_deletar_zips(caminho_pasta_zip: str, caminho_pasta_salvar: str):
    # Converte para caminho absoluto baseado de onde o script está sendo executado
    caminho_pasta_zip_completo = Path(caminho_pasta_zip).resolve()
    caminho_pasta_salvar_completo = Path(caminho_pasta_salvar).resolve()
    
    if not caminho_pasta_zip_completo.exists():
        print(f"❌ Diretório não encontrado: {caminho_pasta_zip_completo}")
        return
        
    # Procura todos os arquivos .zip na pasta
    arquivos_zip = list(caminho_pasta_zip_completo.glob("*.zip"))
    
    if not arquivos_zip:
        print(f"⚠️ Nenhum arquivo .zip encontrado em: {caminho_pasta_zip_completo}")
        return
        
    print(f"📦 Encontrados {len(arquivos_zip)} arquivo(s) compactado(s).\n")
    
    for zip_path in arquivos_zip:
        print(f"⏳ Extraindo: {zip_path.name} ...")
        try:
            # Abre e extrai o arquivo
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(caminho_pasta_salvar_completo)
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
    CAMINHO_DADOS_SALVAR = "data/raw"
    CAMINHO_DADOS_DOWNLOAD = "data/download"
    extrair_e_deletar_zips(
        caminho_pasta_zip=CAMINHO_DADOS_DOWNLOAD,
        caminho_pasta_salvar=CAMINHO_DADOS_SALVAR
    )
