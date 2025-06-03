from .builder import Festa

class FestaUtils:
    @staticmethod
    def gerarConvite(festa: Festa) -> str:
        return f"""
        ================================
               CONVITE PARA A FESTA
        ================================
        🎉 Nome do Aniversariante: {festa.nomeAniversariante}
        📍 Local: {festa.local}
        📅 Data: {festa.data.strftime('%d/%m/%Y')}
        ⏰ Hora: {festa.hora.strftime('%H:%M')}
        🔗 Link do Grupo: {festa.linkGrupo or 'Não informado'}
        ================================
        """

    @staticmethod
    def gerarPreferencias(festa: Festa) -> str:
        return f"""
        ================================
           PREFERÊNCIAS DA FESTA
        ================================
        🍴 Buffet: {', '.join(festa.buffet)}
        🎵 Estilos Musicais: {', '.join(festa.estilosMusicais)}
        ================================
        """
