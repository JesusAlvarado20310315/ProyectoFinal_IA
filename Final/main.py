import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    
    @bot.group()
    async def carreras(ctx):
        """Carreras del ceti"""
        if ctx.invoked_subcommand is None:
            await ctx.send(f"{ctx.subcommand_passed} No es una carrera del Ceti Colomos")
    
    @carreras.command()
    async def industrial(ctx):
        await ctx.send("Malla curricular: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20Industrial/2019/Malla%20Curricular/Malla%20Curricular%20Ingenier%C3%ADa_Industrial.pdf"
                       "\nPlan de estudios: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20Industrial/2019/Plan%20de%20estudios/PE%20Ingenier%C3%ADa%20Industrial.pdf"
                       "\nPrograma: https://direccionacademica.ceti.mx/ingenieria/ing_industrial.php#multiCollapseExample2")
    
    @carreras.command()
    async def mecatronica(ctx):
        await ctx.send("Malla curricular: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20Mecatronica/2019/Malla%20Curricular/Malla%20Mecatronica.pdf"
                       "\nPlan de estudios: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20Mecatronica/2019/Plan%20de%20estudios/PE%20Mecatr%C3%B3nica.pdf"
                       "\nPrograma: https://direccionacademica.ceti.mx/ingenieria/ing_mecatronica.php#multiCollapseExample2")
    
    @carreras.command()
    async def diseñoelectrónico(ctx):
        await ctx.send("Malla curricular: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20en%20Diseno%20Electronico%20y%20Sistemas%20Inteligentes/2019/Malla%20Curricular/Ingenieria_Diseno_Electronico_Sistemas_Inteligentes.pdf"
                       "\nPlan de estudios: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20en%20Diseno%20Electronico%20y%20Sistemas%20Inteligentes/2019/Plan%20de%20estudios/PE%20IDESI.pdf"
                       "\nPrograma: https://direccionacademica.ceti.mx/ingenieria/ing_diseno_electronico_sistemas_inteligentes.php#multiCollapseExample2")
        
    @carreras.command()
    async def desarrollosoftware(ctx):
        await ctx.send("Malla curricular: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20en%20Desarrollo%20de%20Software/2019/Plan%20de%20estudios/PE%20IDS.pdf"
                       "\nPlan de estudios: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20en%20Desarrollo%20de%20Software/2019/Plan%20de%20estudios/PE%20IDS.pdf"
                       "\nPrograma: https://direccionacademica.ceti.mx/ingenieria/ing_desarrollo_software.php#multiCollapseExample2")
        
    @carreras.command()
    async def civilsustentable(ctx):
        await ctx.send("Malla curricular: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20Civil%20Sustentable/2019/Malla%20Curricular/Ingenieria_Civil_Sustentable.pdf"
                       "\nPlan de estudios: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20Civil%20Sustentable/2019/Plan%20de%20estudios/PE%20CIVIL%20SUSTENTABLE.pdf"
                       "\nPrograma: https://direccionacademica.ceti.mx/ingenieria/ing_civil_sustentable.php#multiCollapseExample2")
        
    @carreras.command()
    async def tecnologiasoftware(ctx):
        await ctx.send("Malla curricular: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20en%20Tecnologia%20de%20Software/2019/Malla%20Curricular/Malla%20Curricular%20ITS.pdf"
                       "\nPlan de estudios: https://direccionacademica.ceti.mx/docs/Planes%20y%20Programas%20de%20Estudio/Ingenieria/Ingenieria%20en%20Tecnologia%20de%20Software/2019/Plan%20de%20estudios/PE%20ITS.pdf"
                       "\nPrograma: https://direccionacademica.ceti.mx/ingenieria/ing_tecnologia_software.php#multiCollapseExample2")
    
    @bot.group()
    async def materias(ctx):
        """Todas las materias por carrera"""
        if ctx.invoked_subcommand is None:
            await ctx.send(f"{ctx.subcommand_passed} No es una carrera del Ceti Colomos")
        
    @materias.command()
    async def m_industrial_1(ctx):
        await ctx.send("Semestre 1"
                       "\nProgramación estructurada\nÉtica profesional\nFilosofías, modelos y sistemas de calidad\nMedio ambiente y desarrollo sustentable"
                       "\nProceso administrativo y desarrollo organizacional\nPrécalculo\nQuímica\nInglés I"
                       "\nSemestre 2"
                       "\nCalidad en servicio y MPG, función inspección, auditoría\nÁlgebra lineal\nInglés II\nMediciones en ingeniería\nEstática"
                       "\nCálculo diferencial e integral\nAdministración de recursos\nElementos y ciencias de los materiales"
                       "\nSemestre 3"
                       "\nProbabilidad y estadística\nIngles III\nElectricidad y magnetismo\nMecánica de fluidos\nTermodinámica aplicada\nEcuaciones diferenciales"
                       "\nHerramientas núcleo, ingeniería de calidad y plan de calidad\nDinámica"
                       "\nSemestre 4"
                       "\nControl estadístico del proceso, ingeniería de procesos y la ruta de calidad\nCircuitos eléctricos\nInglés IV"
                       "\nDibujo asistido por computadora\nMétodos numéricos\nHabilidades críticas de la investigación\nProbabilidad y estadística II"
                       "\nCálculo de varias variables\nÓptica y acústica")
        
    @materias.command()
    async def m_industrial_2(ctx):
        await ctx.send("\nSemestre 5"
                       "\nInvestigación de operaciones I\nPlaneación estratégica y habilidades directivas\nCostos en ingeniería\nMáquinas eléctricas"
                       "\nInglés V\nIntroducción a la economía\nSix sigma y diseño para six sigma\nIngeniería de métodos y ergonomía"
                       "\nSemestre 6"
                       "\nAnálisis y diseño de sistemas lean manufacturing\nProcesos Industriales\nInvestigación de operaciones II\nIngeniería económica"
                       "\nAdministración de operaciones I\nInglés VI\nInnovación en la mercadotecnia de productos, procesos y servicios"
                       "\nSemestre 7"
                       "\nDiseño y gestión del TPM y RCM en industria 4.0\nInnovación y habilidades emprendedoras\nProceso de manufactura\nInglés VII"
                       "\nAdministración de operaciones II\nAdministración de operaciones II\nInstalaciones industriales y seguridad industrial"
                       "\nAnálisis de decisiones"
                       "\nSemestre 8"
                       "\nDiseño, gestión y evaluación de proyectos\nRelaciones industriales y legislación laboral"
                       "\nDiseño y gestión de sistemas de trabajo, nuevos productos, acreditación y certificación"
                       "\nDiseño y gestión de sistemas de manufactura con simulación\nDiseño y administración de la cadena de suministro\nTaller de desarrollo humano")
        
    @bot.group()
    async def especializaciones_indus(ctx):
        """Especializaciones de la carrea de Industrial"""
        if ctx.invoked_subcommand is None:
            await ctx.send(f"{ctx.subcommand_passed} No es una especializacion de Ingenieria Industrial")
    
    @especializaciones_indus.command()
    async def control(ctx):
        await ctx.send("\nSemestre 5"
                       "\nElectrónica industrial [Área especializante I de Control e instrumentación]"
                       "\nSemestre 6"
                       "\nInstrumentación industrial [Área especializante II de Control e instrumentación]"
                       "\nSemestre 7"
                       "\nIntroducción a control [Área especializante III de Control e instrumentación]"
                       "\nControl de procesos [Área especializante IV de Control e instrumentación"
                       "\nSemestre 8"
                       "\nAutomatización [Área especializante V de Control e instrumentación]"
                       "\nRobótica industrial [Área especializante VI de Control e instrumentación]"
                       "\nControl industrial [Área especializante VII de Control e instrumentación]")
        
    @especializaciones_indus.command()
    async def sistemas(ctx):
        await ctx.send("\nSemestre 5"
                       "\nSistemas mecánicos [Área especializante I de Sistemas mecánicos]"
                       "\nSemestre 6"
                       "\nAutomatización de mecanismos [Área especializante II de Sistemas mecánicos]"
                       "\nSemestre 7"
                       "\nCAE [Área especializante III de Sistemas mecánicos]"
                       "\nResistencia y aplicación [Área especializante IV de Sistemas mecánicos]"
                       "\nSemestre 8"
                       "\nDesarrollo de producto [Área especializante V de Sistemas mecánicos]"
                       "\nMetrología dimensional [Área especializante VI de Sistemas mecánicos]"
                       "\nDiseño y modelado de máquina [Área especializante VII de Sistemas mecánicos]")
    
            
    @bot.group()
    async def calificaciones(ctx):
        """Cuanto te falta para pasar la materia"""
        if ctx.invoked_subcommand is None:
            await ctx.send(f"{ctx.subcommand_passed} No es un tipo de evaluacion del Ceti")
    
    calificacion_aprobatoria = 70
    califiacion_max = 100
    
    @calificaciones.command()
    async def A(ctx, one : float, two: float):
        peso1 = 0.2  # Peso del primer parcial
        peso2 = 0.35  # Peso del segundo parcial
        peso3 = 0.45  # Peso del tercer parcial
        parcial3 = (calificacion_aprobatoria - (one*peso1 + two*peso2)) / peso3
        if parcial3<califiacion_max:
            await ctx.send(parcial3)
        else:
            await ctx.send("No pasa la materia")
        
    @calificaciones.command()
    async def B(ctx, one : float, two: float):
        peso1 = 0.15  # Peso del primer parcial
        peso2 = 0.35  # Peso del segundo parcial
        peso3 = 0.50  # Peso del tercer parcial
        parcial3 = (calificacion_aprobatoria - (one*peso1 + two*peso2)) / peso3
        if parcial3<califiacion_max:
            await ctx.send(parcial3)
        else:
            await ctx.send("No pasa la materia")
        
    @calificaciones.command()
    async def C(ctx, one : float, two: float):
        peso1 = 0.33  # Peso del primer parcial
        peso2 = 0.33  # Peso del segundo parcial
        peso3 = 0.34  # Peso del tercer parcial
        parcial3 = (calificacion_aprobatoria - (one*peso1 + two*peso2)) / peso3
        if parcial3<califiacion_max:
            await ctx.send(parcial3)
        else:
            await ctx.send("No pasa la materia")
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)
    
if __name__ == "__main__":
    run()